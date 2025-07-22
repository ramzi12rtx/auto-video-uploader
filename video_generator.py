from moviepy.editor import TextClip, CompositeVideoClip

def generate_video(text="هذا فيديو تلقائي"):
    clip = TextClip(text, fontsize=70, color='white', size=(1280, 720)).set_duration(10)
    video = CompositeVideoClip([clip])
    video.write_videofile("output.mp4", fps=24)
