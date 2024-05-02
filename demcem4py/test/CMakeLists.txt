cmake_minimum_required(VERSION 3.11)

# Fetch DEMCEM source code
include(FetchContent)
FetchContent_Declare(
  demcem
  GIT_REPOSITORY https://github.com/thanospol/DEMCEM.git
  GIT_TAG 4b8e2c915eb33fda229b714bf04a49666795835c
)
FetchContent_MakeAvailable(demcem)

project(demcem_example_runner LANGUAGES CXX)

add_executable(demcem_example_runner demcem_example_runner.cpp)

# Files and directories for SS_EA_nxRWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_SS_EA_nxRWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/coefficients_ss_ea_nxrwg.cpp
    ${source_path}/demcem_ss_ea_nxrwg.cpp
    ${source_path}/psi_limits_ss_ea_nxrwg.cpp
    ${source_path}/theta_limits_ss_ea_nxrwg.cpp
    ${source_path}/x1_ss_ea_nxrwg.cpp
    ${source_path}/x2_ss_ea_nxrwg.cpp
    ${source_path}/x_function_pre_ss_ea_nxrwg.cpp
    ${source_path}/x_functions_ss_ea_nxrwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Files and directories for SS_EA_RWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_SS_EA_RWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/coefficients_ss_ea_rwg.cpp
    ${source_path}/theta_limits_ss_ea_rwg.cpp
    ${source_path}/x2_ss_ea_rwg.cpp
    ${source_path}/x_functions_ss_ea_rwg.cpp
    ${source_path}/demcem_ss_ea_rwg.cpp
    ${source_path}/psi_limits_ss_ea_rwg.cpp
    ${source_path}/x1_ss_ea_rwg.cpp
    ${source_path}/x_functions_pre_ss_ea_rwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Files and directories for SS_VA_nxRWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_SS_VA_nxRWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/coefficients_ss_va_nxrwg.cpp
    ${source_path}/demcem_ss_va_nxrwg.cpp
    ${source_path}/k_functions_ss_va_nxrwg.cpp
    ${source_path}/omega_functions_ss_va_nxrwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Files and directories for SS_VA_RWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_SS_VA_RWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/coefficients_ss_va_rwg.cpp
    ${source_path}/demcem_ss_va_rwg.cpp
    ${source_path}/k_functions_ss_va_rwg.cpp
    ${source_path}/omega_functions_ss_va_rwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Files and directories for WS_EA_RWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_WS_EA_RWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/coefficients_ws_ea_rwg.cpp
    ${source_path}/demcem_ws_ea_rwg.cpp
    ${source_path}/psi_limits_ws_ea_rwg.cpp
    ${source_path}/theta_limits_ws_ea_rwg.cpp
    ${source_path}/x1_ws_ea_rwg.cpp
    ${source_path}/x2_ws_ea_rwg.cpp
    ${source_path}/x_functions_pre_ws_ea_rwg.cpp
    ${source_path}/x_functions_ws_ea_rwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Files and directories for WS_ST_RWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_WS_ST_RWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/demcem_ws_st_rwg.cpp
    ${source_path}/phi_functions_ws_st_rwg.cpp
    ${source_path}/phi_ws_st_rwg.cpp
    ${source_path}/post_ws_st_rwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Files and directories for WS_VA_RWG
set(source_path "${demcem_SOURCE_DIR}/src/c++/DEMCEM_WS_VA_RWG")
target_sources(demcem_example_runner PRIVATE
    ${source_path}/coefficients_ws_va_rwg.cpp
    ${source_path}/demcem_ws_va_rwg.cpp
    ${source_path}/k_functions_ws_va_rwg.cpp
    ${source_path}/omega_functions_ws_va_rwg.cpp
)
target_include_directories(demcem_example_runner PRIVATE ${source_path})

# Miscellaneous files and directories
target_include_directories(demcem_example_runner PRIVATE ${demcem_SOURCE_DIR}/src/c++/Examples)
target_sources(demcem_example_runner PRIVATE ${demcem_SOURCE_DIR}/src/c++/Examples/gl_quad.cpp)
