name = "ffmpeg"

version = "6.1.0.sse.1.3.0"

authors = [
    "FFmpeg"
]

description = \
    """
    FFmpeg is a collection of libraries and tools to process multimedia content such
    as audio, video, subtitles and related metadata.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "nasm",
    "yasm",
    "x264",
    "x265",
    "libpng",
    "freetype",
    "harfbuzz",
    "zimg",
    # "libmp3lame",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
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
