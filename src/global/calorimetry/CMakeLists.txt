cmake_minimum_required(VERSION 3.16)

get_filename_component(PLUGIN_NAME ${CMAKE_CURRENT_LIST_DIR} NAME)
print_header(">>>>   P L U G I N :   ${PLUGIN_NAME}    <<<<")       # Fancy printing

# Function creates ${PLUGIN_NAME}_plugin and ${PLUGIN_NAME}_library targets
# Setting default includes, libraries and installation paths

plugin_add(${PLUGIN_NAME} WITH_STATIC_LIBRARY)

# The macro grabs sources as *.cc *.cpp *.c and headers as *.h *.hh *.hpp
# Then correctly sets sources for ${_name}_plugin and ${_name}_library targets
# Adds headers to the correct installation directory
plugin_glob_all(${PLUGIN_NAME})

# Find dependencies
find_package(EDM4HEP REQUIRED)
find_package(EDM4EIC REQUIRED)
find_package(podio REQUIRED)
find_package(DD4hep REQUIRED)

set(EDM4EIC_INCLUDE_DIR ${EDM4EIC_DIR}/../../include)

# Add include directories (works same as target_include_directories)
plugin_include_directories(${PLUGIN_NAME} SYSTEM PUBLIC ${podio_INCLUDE_DIR} ${EDM4EIC_INCLUDE_DIR})

# Add libraries (works same as target_include_directories)
plugin_link_libraries(${PLUGIN_NAME} dd4hep_library EDM4HEP::edm4hep DD4hep::DDCore calorimetry_algorithms_library)
