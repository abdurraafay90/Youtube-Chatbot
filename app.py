import re
import chainlit as cl
from youtube_utils import extract_video_id, get_transcript, build_vectorstore, create_chain

@cl.on_chat_start
async def start():
    await cl.Message(content="🎥 Send me a YouTube link, and I’ll answer questions about it!").send()


@cl.on_message
async def handle_message(message: cl.Message):
    text = message.content.strip()

    video_id = extract_video_id(text)
    if not video_id:
        if len(text) == 11 and re.fullmatch(r"[0-9A-Za-z_-]{11}", text):
            video_id = text

    if video_id:
        await cl.Message(content=f"Loading transcript for `{video_id}`... Please wait.").send()

        transcript = get_transcript(video_id)
        if not transcript:
            await cl.Message(content=" No transcript found or it's disabled for this video.").send()
            return

        try:
            retriever = build_vectorstore(transcript)
            chain = create_chain(retriever)
            cl.user_session.set("chain", chain)
            await cl.Message(content=" Transcript loaded! You can now ask questions about the video.").send()
        except Exception as e:
            await cl.Message(content=f" Error while building chain: {e}").send()
        return
    
    chain = cl.user_session.get("chain")
    if not chain:
        await cl.Message(content=" Please send a YouTube link first!").send()
        return

    question = text
    msg = cl.Message(content="🤖 Thinking...")
    await msg.send()

    try:
        for chunk in chain.stream(question):
            if hasattr(chunk, "content"):
                await msg.stream_token(chunk.content)
            else:
                await msg.stream_token(str(chunk))

        await msg.update()

    except Exception as e:
        msg.content = f" Error generating answer: {e}"
        await msg.update()
