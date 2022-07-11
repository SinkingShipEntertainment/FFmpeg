name = "ffmpeg"

# Remember to modify the commands function here
version = "5.0.1"

authors = [
    "FFmpeg"
]

description = \
    """
    FFmpeg is a collection of libraries and tools to process multimedia content such
    as audio, video, subtitles and related metadata.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "nasm",
    "yasm",
    "x264",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

uuid = "repository.FFmpeg"

# NOTE:
# rez-build -i --build-system cmake
# rez-release --build-system cmake

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
