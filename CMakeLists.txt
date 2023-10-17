CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


message($ENV{PKG_CONFIG_PATH})

# Possible configure settings (needs research):
#--disable-asm
#--enable-libmp3lame is causing configuration errors. If trying, make sure "libmp3lame" is a requirement in REZ


# Missing libs for xstudio
# --enable-libfdk_aac
# --enable-libmp3lame
# --enable-libopus
# --enable-libvpx
# --enable-libx265

ExternalProject_add(
    ffmpeg
    SOURCE_DIR ${CMAKE_SOURCE_DIR}
    PREFIX ffmpeg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_SOURCE_DIR}/configure
        --prefix=${CMAKE_INSTALL_PREFIX}
        --extra-libs=-lpthread
        --extra-libs=-lm
        --disable-doc
        --enable-gpl
        --enable-version3
        --enable-nonfree
        --enable-shared
        --enable-libx264
        --enable-decoder=mp3
        --enable-libfontconfig
        --enable-libfreetype
        --enable-libharfbuzz
        --enable-libzimg
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make ${make_args}
)

# Necessary so REZ can create a `make install` target
rez_install_files(
    Changelog
    DESTINATION .
)
