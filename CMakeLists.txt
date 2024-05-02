cmake_minimum_required(VERSION 3.11)

project(demcem4py LANGUAGES CXX)

find_package(pybind11 REQUIRED)
pybind11_add_module(demcem4py demcem4py/demcem4py.cpp)

# Files and directories for SS_EA_nxRWG
set(source_path "DEMCEM_src/c++/DEMCEM_SS_EA_nxRWG")
target_sources(demcem4py PRIVATE
    ${source_path}/coefficients_ss_ea_nxrwg.cpp
    ${source_path}/demcem_ss_ea_nxrwg.cpp
    ${source_path}/psi_limits_ss_ea_nxrwg.cpp
    ${source_path}/theta_limits_ss_ea_nxrwg.cpp
    ${source_path}/x1_ss_ea_nxrwg.cpp
    ${source_path}/x2_ss_ea_nxrwg.cpp
    ${source_path}/x_function_pre_ss_ea_nxrwg.cpp
    ${source_path}/x_functions_ss_ea_nxrwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Files and directories for SS_EA_RWG
set(source_path "DEMCEM_src/c++/DEMCEM_SS_EA_RWG")
target_sources(demcem4py PRIVATE
    ${source_path}/coefficients_ss_ea_rwg.cpp
    ${source_path}/theta_limits_ss_ea_rwg.cpp
    ${source_path}/x2_ss_ea_rwg.cpp
    ${source_path}/x_functions_ss_ea_rwg.cpp
    ${source_path}/demcem_ss_ea_rwg.cpp
    ${source_path}/psi_limits_ss_ea_rwg.cpp
    ${source_path}/x1_ss_ea_rwg.cpp
    ${source_path}/x_functions_pre_ss_ea_rwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Files and directories for SS_VA_nxRWG
set(source_path "DEMCEM_src/c++/DEMCEM_SS_VA_nxRWG")
target_sources(demcem4py PRIVATE
    ${source_path}/coefficients_ss_va_nxrwg.cpp
    ${source_path}/demcem_ss_va_nxrwg.cpp
    ${source_path}/k_functions_ss_va_nxrwg.cpp
    ${source_path}/omega_functions_ss_va_nxrwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Files and directories for SS_VA_RWG
set(source_path "DEMCEM_src/c++/DEMCEM_SS_VA_RWG")
target_sources(demcem4py PRIVATE
    ${source_path}/coefficients_ss_va_rwg.cpp
    ${source_path}/demcem_ss_va_rwg.cpp
    ${source_path}/k_functions_ss_va_rwg.cpp
    ${source_path}/omega_functions_ss_va_rwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Files and directories for WS_EA_RWG
set(source_path "DEMCEM_src/c++/DEMCEM_WS_EA_RWG")
target_sources(demcem4py PRIVATE
    ${source_path}/coefficients_ws_ea_rwg.cpp
    ${source_path}/demcem_ws_ea_rwg.cpp
    ${source_path}/psi_limits_ws_ea_rwg.cpp
    ${source_path}/theta_limits_ws_ea_rwg.cpp
    ${source_path}/x1_ws_ea_rwg.cpp
    ${source_path}/x2_ws_ea_rwg.cpp
    ${source_path}/x_functions_pre_ws_ea_rwg.cpp
    ${source_path}/x_functions_ws_ea_rwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Files and directories for WS_ST_RWG
set(source_path "DEMCEM_src/c++/DEMCEM_WS_ST_RWG")
target_sources(demcem4py PRIVATE
    ${source_path}/demcem_ws_st_rwg.cpp
    ${source_path}/phi_functions_ws_st_rwg.cpp
    ${source_path}/phi_ws_st_rwg.cpp
    ${source_path}/post_ws_st_rwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Files and directories for WS_VA_RWG
set(source_path "DEMCEM_src/c++/DEMCEM_WS_VA_RWG")
target_sources(demcem4py PRIVATE
    ${source_path}/coefficients_ws_va_rwg.cpp
    ${source_path}/demcem_ws_va_rwg.cpp
    ${source_path}/k_functions_ws_va_rwg.cpp
    ${source_path}/omega_functions_ws_va_rwg.cpp
)
target_include_directories(demcem4py PRIVATE ${source_path})

# Miscellaneous files and directories
target_include_directories(demcem4py PRIVATE DEMCEM_src/c++/Examples)
target_sources(demcem4py PRIVATE DEMCEM_src/c++/Examples/gl_quad.cpp)

install(TARGETS demcem4py DESTINATION .)# ${CMAKE_CURRENT_SOURCE_DIR})
