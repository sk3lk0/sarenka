from typing import Dict, Tuple, Sequence, List, NoReturn
import subprocess

import json
class Hardware:
    @staticmethod
    def get_bios()->Dict:
        """
        Returns Bios version
        """
        value =  subprocess.getoutput("wmic bios get smbiosbiosversion")
        response =  {
            "name" : value.split()[0],
            "version": value.split()[1]
        }
        return response






    @staticmethod
    def get_computer_information()->Dict:
        """
        Returns name computer_information
        """
        name_computer =  subprocess.getoutput("wmic computersystem get name,systemtype")

        computer_serial_number =  subprocess.getoutput("wmic bios get serialnumber")
        total_physical_memory =  subprocess.getoutput("wmic COMPUTERSYSTEM get TotalPhysicalMemory")
        mac_address =  subprocess.getoutput("wmic nic get macaddress")
        computer_manufacturer =  subprocess.getoutput("WMIC COMPUTERSYSTEM GET MANUFACTURER")
        response =  {
            "name" : name_computer.split()[2],
            "system_type": name_computer.split()[3],
            "computer_serial_number" : computer_serial_number.split()[1],
            "total_physical_memory" : total_physical_memory.split()[1],
            "mac_address" : mac_address.split()[1],
            "computer_manufacturer" : ' '.join(computer_manufacturer.split()[1:]),

        }
        return response
    


    @staticmethod
    def get_motherboard_information()->Dict:
        """
        Returns name motherboard_information
        """
        product =  subprocess.getoutput("wmic baseboard get product")
        manufacturer =  subprocess.getoutput("wmic baseboard get manufacturer")
        version =  subprocess.getoutput("wmic baseboard get version")
        serialnumber =  subprocess.getoutput("wmic baseboard get serialnumber")

        response =  {
            "product" : product.split()[1],
            "manufacturer" : ' '.join(manufacturer.split()[1:]),
            "version" : version.split()[1],
            "serialnumber" : serialnumber.split()[1],

        }
        return response
        


    @staticmethod
    def get_operation_system()->Dict:
        """
        Returns name operation_system
        """
        os_architecture =  subprocess.getoutput("wmic OS get OSArchitecture")
        other_information =  subprocess.getoutput('systeminfo | findstr /C:"OS"')
        other_information =dict(map(str.strip, sub.split(':', 1)) for sub in other_information.split('\n') if ':' in sub)
        response =  {
            "name" : other_information["OS Name"],
            "version" : other_information["OS Version"],
            "manufacturer" : other_information["OS Manufacturer"],
            "configuration" : other_information["OS Configuration"],
            "build_type" : other_information["OS Build Type"],
            "os_architecture" : os_architecture.split()[1],

        }

        return response




    @staticmethod
    def get_hard_drive_info()->Dict:
        """
        Returns name hard_drive_info
        """
        hard_drive =  subprocess.getoutput("wmic logicaldisk where drivetype=3 get name, freespace, systemname, filesystem, size, volumeserialnumber")
        hard_drive2 =hard_drive.split()[6:]
        
        response={}
        x = range(0, 6, len(hard_drive))

        for n in x:
            hard_drive_element=hard_drive2[n+1:n+6]
            response[hard_drive2[n]]={
                "freespace":hard_drive_element[0],
                "systemname":hard_drive_element[1],
                "filesystem":hard_drive_element[2],
                "size":hard_drive_element[3],
                "volumeserialnumber":hard_drive_element[4],

                }
        return response



    @staticmethod
    def to_json()->Dict:
        response = {}
        response.update({"bios": Hardware.get_bios()})
        response.update({"computer_information": Hardware.get_computer_information()})
        response.update({"operation_system": Hardware.get_operation_system()})
        response.update({"motherboard_information": Hardware.get_motherboard_information()})
        response.update({"hard_drive_info": Hardware.get_hard_drive_info()})

        return response  