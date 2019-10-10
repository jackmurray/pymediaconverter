import subprocess
from .celerysetup import app


@app.task
def celery_convert_audio(filename, outputfilename, targetbitrate):
    subprocess.run(["ffmpeg", "-i", filename, "-b:a", str(targetbitrate) + "k", outputfilename])
