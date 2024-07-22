from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType

RUIJIE_DEVICE_TYPES: dict[str, "DeviceType"] = {
    "1.3.6.1.4.1.4881.1.1.10.1.1": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126G"},
    "1.3.6.1.4.1.4881.1.1.10.1.106": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2628G-E"},
    "1.3.6.1.4.1.4881.1.1.10.1.11": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S21-STACKING"},
    "1.3.6.1.4.1.4881.1.1.10.1.12": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3550-24"},
    "1.3.6.1.4.1.4881.1.1.10.1.13": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3550-48"},
    "1.3.6.1.4.1.4881.1.1.10.1.15": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3550-12SFP-GT"},
    "1.3.6.1.4.1.4881.1.1.10.1.16": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6806"},
    "1.3.6.1.4.1.4881.1.1.10.1.17": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6810"},
    "1.3.6.1.4.1.4881.1.1.10.1.18": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126S"},
    "1.3.6.1.4.1.4881.1.1.10.1.19": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126S-STACKING"},
    "1.3.6.1.4.1.4881.1.1.10.1.2": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126GL3"},
    "1.3.6.1.4.1.4881.1.1.10.1.20": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S1908PLUS"},
    "1.3.6.1.4.1.4881.1.1.10.1.21": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S1916PLUS"},
    "1.3.6.1.4.1.4881.1.1.10.1.22": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6506"},
    "1.3.6.1.4.1.4881.1.1.10.1.23": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126S-08"},
    "1.3.6.1.4.1.4881.1.1.10.1.24": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126S-16"},
    "1.3.6.1.4.1.4881.1.1.10.1.25": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6806E"},
    "1.3.6.1.4.1.4881.1.1.10.1.26": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6810E"},
    "1.3.6.1.4.1.4881.1.1.10.1.27": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2026G"},
    "1.3.6.1.4.1.4881.1.1.10.1.28": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750-24"},
    "1.3.6.1.4.1.4881.1.1.10.1.29": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750-48"},
    "1.3.6.1.4.1.4881.1.1.10.1.3": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2150G"},
    "1.3.6.1.4.1.4881.1.1.10.1.30": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126"},
    "1.3.6.1.4.1.4881.1.1.10.1.31": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2126-STACKING"},
    "1.3.6.1.4.1.4881.1.1.10.1.32": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2026F"},
    "1.3.6.1.4.1.4881.1.1.10.1.33": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3760-48"},
    "1.3.6.1.4.1.4881.1.1.10.1.34": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3760-12SFP-GT"},
    "1.3.6.1.4.1.4881.1.1.10.1.35": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S4009"},
    "1.3.6.1.4.1.4881.1.1.10.1.36": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3526"},
    "1.3.6.1.4.1.4881.1.1.10.1.37": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3512G"},
    "1.3.6.1.4.1.4881.1.1.10.1.38": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-12GCS-L3"},
    "1.3.6.1.4.1.4881.1.1.10.1.39": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-24GS-L3"},
    "1.3.6.1.4.1.4881.1.1.10.1.4": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2150GL3"},
    "1.3.6.1.4.1.4881.1.1.10.1.40": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-48TMS-2S-S"},
    "1.3.6.1.4.1.4881.1.1.10.1.41": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750-24GT-12SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.42": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750P-24GT-12SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.43": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S8606"},
    "1.3.6.1.4.1.4881.1.1.10.1.44": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S8610"},
    "1.3.6.1.4.1.4881.1.1.10.1.45": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S9610"},
    "1.3.6.1.4.1.4881.1.1.10.1.46": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S9620"},
    "1.3.6.1.4.1.4881.1.1.10.1.47": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2924"},
    "1.3.6.1.4.1.4881.1.1.10.1.48": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3760-24"},
    "1.3.6.1.4.1.4881.1.1.10.1.49": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3760-48V2"},
    "1.3.6.1.4.1.4881.1.1.10.1.5": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S4909"},
    "1.3.6.1.4.1.4881.1.1.10.1.50": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750E-24"},
    "1.3.6.1.4.1.4881.1.1.10.1.51": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750E-48"},
    "1.3.6.1.4.1.4881.1.1.10.1.52": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750E-12SFP-GT"},
    "1.3.6.1.4.1.4881.1.1.10.1.53": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750S-24GT-12SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.54": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2128G"},
    "1.3.6.1.4.1.4881.1.1.10.1.55": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2927XG"},
    "1.3.6.1.4.1.4881.1.1.10.1.56": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3512GPLUS"},
    "1.3.6.1.4.1.4881.1.1.10.1.57": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6604"},
    "1.3.6.1.4.1.4881.1.1.10.1.58": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6606"},
    "1.3.6.1.4.1.4881.1.1.10.1.59": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S6610"},
    "1.3.6.1.4.1.4881.1.1.10.1.6": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3550-12G"},
    "1.3.6.1.4.1.4881.1.1.10.1.60": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750-24SFP-12GT"},
    "1.3.6.1.4.1.4881.1.1.10.1.61": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750-48GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.62": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750S-48GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.63": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2328G"},
    "1.3.6.1.4.1.4881.1.1.10.1.64": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3250-48"},
    "1.3.6.1.4.1.4881.1.1.10.1.66": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2951XG"},
    "1.3.6.1.4.1.4881.1.1.10.1.67": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750-24-UB"},
    "1.3.6.1.4.1.4881.1.1.10.1.68": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3750-48-UB"},
    "1.3.6.1.4.1.4881.1.1.10.1.69": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "SCG5510"},
    "1.3.6.1.4.1.4881.1.1.10.1.70": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2052G"},
    "1.3.6.1.4.1.4881.1.1.10.1.71": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2352G"},
    "1.3.6.1.4.1.4881.1.1.10.1.72": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S8614"},
    "1.3.6.1.4.1.4881.1.1.10.1.73": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5650-24GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.74": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5650-27XG"},
    "1.3.6.1.4.1.4881.1.1.10.1.75": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5650-51XG"},
    "1.3.6.1.4.1.4881.1.1.10.1.76": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5450-28GT"},
    "1.3.6.1.4.1.4881.1.1.10.1.77": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3760E-24"},
    "1.3.6.1.4.1.4881.1.1.10.1.78": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3250P-24"},
    "1.3.6.1.4.1.4881.1.1.10.1.79": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2928G"},
    "1.3.6.1.4.1.4881.1.1.10.1.8": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3550-24G"},
    "1.3.6.1.4.1.4881.1.1.10.1.80": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2952G"},
    "1.3.6.1.4.1.4881.1.1.10.1.81": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2028G"},
    "1.3.6.1.4.1.4881.1.1.10.1.82": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2528G"},
    "1.3.6.1.4.1.4881.1.1.10.1.83": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S2552G"},
    "1.3.6.1.4.1.4881.1.1.10.1.84": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750R-48GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.85": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750P-48GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.86": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750R-24GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.87": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750P-24GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.88": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750-24GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.89": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750S-24GT-4SFP"},
    "1.3.6.1.4.1.4881.1.1.10.1.92": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750-48GT-4SFP-A"},
    "1.3.6.1.4.1.4881.1.1.10.1.93": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S5750-48GT-4SFP-AP"},
    "1.3.6.1.4.1.4881.1.1.10.1.95": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NM2X-24ESW"},
    "1.3.6.1.4.1.4881.1.1.10.1.96": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NM2X-16ESW"},
    "1.3.6.1.4.1.4881.1.1.10.1.98": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "S3760E-24"},
    "1.3.6.1.4.1.4881.1.2.1.1.1": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2620"},
    "1.3.6.1.4.1.4881.1.2.1.1.10": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2632"},
    "1.3.6.1.4.1.4881.1.2.1.1.11": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R1762"},
    "1.3.6.1.4.1.4881.1.2.1.1.12": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RCMS"},
    "1.3.6.1.4.1.4881.1.2.1.1.13": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-R1762"},
    "1.3.6.1.4.1.4881.1.2.1.1.14": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-R2632"},
    "1.3.6.1.4.1.4881.1.2.1.1.15": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-R2692"},
    "1.3.6.1.4.1.4881.1.2.1.1.16": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-R3642"},
    "1.3.6.1.4.1.4881.1.2.1.1.17": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "HCL-R3662"},
    "1.3.6.1.4.1.4881.1.2.1.1.18": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R3740"},
    "1.3.6.1.4.1.4881.1.2.1.1.19": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NBR2000"},
    "1.3.6.1.4.1.4881.1.2.1.1.2": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2624"},
    "1.3.6.1.4.1.4881.1.2.1.1.20": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NBR300"},
    "1.3.6.1.4.1.4881.1.2.1.1.21": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NBR1200"},
    "1.3.6.1.4.1.4881.1.2.1.1.22": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NBR1500"},
    "1.3.6.1.4.1.4881.1.2.1.1.23": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2716"},
    "1.3.6.1.4.1.4881.1.2.1.1.24": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2724"},
    "1.3.6.1.4.1.4881.1.2.1.1.25": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R3802"},
    "1.3.6.1.4.1.4881.1.2.1.1.26": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R3804"},
    "1.3.6.1.4.1.4881.1.2.1.1.27": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR50-20"},
    "1.3.6.1.4.1.4881.1.2.1.1.28": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR50-40"},
    "1.3.6.1.4.1.4881.1.2.1.1.29": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR50-80"},
    "1.3.6.1.4.1.4881.1.2.1.1.3": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2690"},
    "1.3.6.1.4.1.4881.1.2.1.1.30": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NPE50-20"},
    "1.3.6.1.4.1.4881.1.2.1.1.31": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR10-02"},
    "1.3.6.1.4.1.4881.1.2.1.1.32": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR20-04"},
    "1.3.6.1.4.1.4881.1.2.1.1.33": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "VPN120"},
    "1.3.6.1.4.1.4881.1.2.1.1.34": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NPE80"},
    "1.3.6.1.4.1.4881.1.2.1.1.35": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR20-24"},
    "1.3.6.1.4.1.4881.1.2.1.1.36": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NM2-16ESW"},
    "1.3.6.1.4.1.4881.1.2.1.1.37": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NM2-24ESW"},
    "1.3.6.1.4.1.4881.1.2.1.1.38": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NMX-24ESW"},
    "1.3.6.1.4.1.4881.1.2.1.1.39": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NMX-24ESW-L2"},
    "1.3.6.1.4.1.4881.1.2.1.1.4": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2692"},
    "1.3.6.1.4.1.4881.1.2.1.1.40": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NMX-24ESW-3GEL3"},
    "1.3.6.1.4.1.4881.1.2.1.1.41": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR20-14"},
    "1.3.6.1.4.1.4881.1.2.1.1.42": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR30-44"},
    "1.3.6.1.4.1.4881.1.2.1.1.43": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2700V2V3"},
    "1.3.6.1.4.1.4881.1.2.1.1.44": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R2700V5"},
    "1.3.6.1.4.1.4881.1.2.1.1.45": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NPE50-40"},
    "1.3.6.1.4.1.4881.1.2.1.1.46": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "RSR20-18"},
    "1.3.6.1.4.1.4881.1.2.1.1.5": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R3642"},
    "1.3.6.1.4.1.4881.1.2.1.1.6": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "R3662"},
    "1.3.6.1.4.1.4881.1.2.1.1.7": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NBR1000"},
    "1.3.6.1.4.1.4881.1.2.1.1.8": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "NBR200"},
    "1.3.6.1.4.1.4881.1.2.1.1.9": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "SECVPN100"},
    "1.3.6.1.4.1.4881.1.3.1.1.1": {"manufacturer": "Ruijie", "platform": "ruijie_os", "model": "WGP500"},
}