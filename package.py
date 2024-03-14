name = "ffmpeg"

version = "6.1.1.sse.1.0.0"

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
    "libpng",
    "freetype",
    "harfbuzz",
]

private_build_requires = [
]

variants = [
]

build_system = "cmake"
uuid = "repository.FFmpeg"


def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
