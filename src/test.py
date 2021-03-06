# -*- coding: utf-8 -*-

from skidl import *

set_default_tool(KICAD)  # KiCad is the default library format.
lib_search_paths[KICAD].append("../lib")

# kicad_lib = SchLib("../lib/FIN_HAT_Template.lib", tool=KICAD)  # Open a KiCad library.
# kicad_lib.export("FIN_HAT_Template")  # Export it into a file in SKiDL format.
# skidl_lib = SchLib(
#     "FIN_HAT_Template", tool=SKIDL
# )  # Create a SKiDL library object from the new file.
# if len(skidl_lib) == len(kicad_lib):
#     print("As expected, both libraries have the same number of parts!")
# else:
#     print("Something went wrong!")


def _Users_nicolastzovanis_Documents_balena_repos_Hardware_skidl_balena_fin_examples_hw_hat_template_v1_1_KiCAD_FIN_HAT_Template_sch():

    # ===============================================================================
    # Component templates.
    # ===============================================================================

    FIN_HAT_Template_Co_Processor_Header_FIN_HAT_Template_PinSocket_2x09_P2_54mm_Vertical = Part(
        "FIN_HAT_TEMPLATE",
        "Co-Processor_Header",
        dest=TEMPLATE,
        footprint="FIN HAT Template:PinSocket_2x09_P2.54mm_Vertical",
    )

    FIN_HAT_Template_POE_Header_FIN_HAT_Template_PinSocket_2x02_P2_54mm_Vertical = Part(
        "FIN_HAT_TEMPLATE",
        "POE_Header",
        dest=TEMPLATE,
        footprint="FIN HAT Template:PinSocket_2x02_P2.54mm_Vertical",
    )

    FIN_HAT_Template_Raspberry_Pi_2_3_Default_FIN_HAT_Template_PinSocket_2x20_P2_54mm_Vertical = Part(
        "FIN_HAT_TEMPLATE",
        "Raspberry_Pi_2_3_Default",
        dest=TEMPLATE,
        footprint="FIN HAT Template:PinSocket_2x20_P2.54mm_Vertical",
    )

    FIN_HAT_Template_USB_Header_FIN_HAT_Template_PinSocket_1x04_P2_54mm_Vertical = Part(
        "FIN_HAT_TEMPLATE",
        "USB_Header",
        dest=TEMPLATE,
        footprint="FIN HAT Template:PinSocket_1x04_P2.54mm_Vertical",
    )

    Mechanical_MountingHole_Pad_MountingHole_MountingHole_2_5mm_Pad = Part(
        "Mechanical",
        "MountingHole_Pad",
        dest=TEMPLATE,
        footprint="MountingHole:MountingHole_2.5mm_Pad",
    )

    # ===============================================================================
    # Component instantiations.
    # ===============================================================================

    H1 = Mechanical_MountingHole_Pad_MountingHole_MountingHole_2_5mm_Pad(
        ref="H1", value="MountingHole_Pad"
    )

    H2 = Mechanical_MountingHole_Pad_MountingHole_MountingHole_2_5mm_Pad(
        ref="H2", value="MountingHole_Pad"
    )

    J1 = FIN_HAT_Template_Raspberry_Pi_2_3_Default_FIN_HAT_Template_PinSocket_2x20_P2_54mm_Vertical(
        ref="J1", value="Raspberry_Pi_2_3_Default"
    )

    J2 = FIN_HAT_Template_POE_Header_FIN_HAT_Template_PinSocket_2x02_P2_54mm_Vertical(
        ref="J2", value="POE_Header"
    )

    J3 = FIN_HAT_Template_Co_Processor_Header_FIN_HAT_Template_PinSocket_2x09_P2_54mm_Vertical(
        ref="J3", value="Co-Processor_Header"
    )

    J4 = FIN_HAT_Template_USB_Header_FIN_HAT_Template_PinSocket_1x04_P2_54mm_Vertical(
        ref="J4", value="USB_Header"
    )

    # ===============================================================================
    # Net interconnections between instantiated components.
    # ===============================================================================

    Net("+3V3").connect(J1["1"], J1["17"])

    Net("+5V").connect(J1["2"], J1["4"], J4["1"])

    Net("GND").connect(
        J4["4"],
        J1["6"],
        J1["39"],
        J1["34"],
        J1["30"],
        J1["25"],
        J1["20"],
        J1["14"],
        J1["9"],
        J3["17"],
    )

    Net("Net-(H1-Pad1)").connect(H1["1"])

    Net("Net-(H2-Pad1)").connect(H2["1"])

    Net("Net-(J1-Pad10)").connect(J1["10"])

    Net("Net-(J1-Pad11)").connect(J1["11"])

    Net("Net-(J1-Pad12)").connect(J1["12"])

    Net("Net-(J1-Pad13)").connect(J1["13"])

    Net("Net-(J1-Pad15)").connect(J1["15"])

    Net("Net-(J1-Pad16)").connect(J1["16"])

    Net("Net-(J1-Pad18)").connect(J1["18"])

    Net("Net-(J1-Pad19)").connect(J1["19"])

    Net("Net-(J1-Pad21)").connect(J1["21"])

    Net("Net-(J1-Pad22)").connect(J1["22"])

    Net("Net-(J1-Pad23)").connect(J1["23"])

    Net("Net-(J1-Pad24)").connect(J1["24"])

    Net("Net-(J1-Pad26)").connect(J1["26"])

    Net("Net-(J1-Pad27)").connect(J1["27"])

    Net("Net-(J1-Pad28)").connect(J1["28"])

    Net("Net-(J1-Pad29)").connect(J1["29"])

    Net("Net-(J1-Pad3)").connect(J1["3"])

    Net("Net-(J1-Pad31)").connect(J1["31"])

    Net("Net-(J1-Pad32)").connect(J1["32"])

    Net("Net-(J1-Pad33)").connect(J1["33"])

    Net("Net-(J1-Pad35)").connect(J1["35"])

    Net("Net-(J1-Pad36)").connect(J1["36"])

    Net("Net-(J1-Pad37)").connect(J1["37"])

    Net("Net-(J1-Pad38)").connect(J1["38"])

    Net("Net-(J1-Pad40)").connect(J1["40"])

    Net("Net-(J1-Pad5)").connect(J1["5"])

    Net("Net-(J1-Pad7)").connect(J1["7"])

    Net("Net-(J1-Pad8)").connect(J1["8"])

    Net("Net-(J2-Pad1)").connect(J2["1"])

    Net("Net-(J2-Pad2)").connect(J2["2"])

    Net("Net-(J2-Pad3)").connect(J2["3"])

    Net("Net-(J2-Pad4)").connect(J2["4"])

    Net("Net-(J3-Pad1)").connect(J3["1"])

    Net("Net-(J3-Pad10)").connect(J3["10"])

    Net("Net-(J3-Pad11)").connect(J3["11"])

    Net("Net-(J3-Pad12)").connect(J3["12"])

    Net("Net-(J3-Pad13)").connect(J3["13"])

    Net("Net-(J3-Pad14)").connect(J3["14"])

    Net("Net-(J3-Pad15)").connect(J3["15"])

    Net("Net-(J3-Pad16)").connect(J3["16"])

    Net("Net-(J3-Pad18)").connect(J3["18"])

    Net("Net-(J3-Pad2)").connect(J3["2"])

    Net("Net-(J3-Pad3)").connect(J3["3"])

    Net("Net-(J3-Pad4)").connect(J3["4"])

    Net("Net-(J3-Pad5)").connect(J3["5"])

    Net("Net-(J3-Pad6)").connect(J3["6"])

    Net("Net-(J3-Pad7)").connect(J3["7"])

    Net("Net-(J3-Pad8)").connect(J3["8"])

    Net("Net-(J3-Pad9)").connect(J3["9"])

    Net("Net-(J4-Pad2)").connect(J4["2"])

    Net("Net-(J4-Pad3)").connect(J4["3"])


# ===============================================================================
# Instantiate the circuit and generate the netlist.
# ===============================================================================

if __name__ == "__main__":
    _Users_nicolastzovanis_Documents_balena_repos_Hardware_skidl_balena_fin_examples_hw_hat_template_v1_1_KiCAD_FIN_HAT_Template_sch()
    generate_netlist()
