CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ffmpeg
    SOURCE_DIR ${CMAKE_SOURCE_DIR}
    PREFIX ffmpeg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_SOURCE_DIR}/configure --prefix=${CMAKE_INSTALL_PREFIX} --pkg-config-flags="--static" --extra-libs=-lpthread --extra-libs=-lm --enable-gpl --enable-libx264
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
    BUILD_COMMAND make ${make_args}
)

# Necessary so REZ can create a `make install` target
rez_install_files(
    Changelog
    DESTINATION .
)
