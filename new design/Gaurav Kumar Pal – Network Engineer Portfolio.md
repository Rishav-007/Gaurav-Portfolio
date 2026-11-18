[about](#about)[skills](#skills)[experience](#work)[projects](#projects)[labs](#labs)[contact](#contact)

gaurav@netlab: \~

$

**2+**years in networking

**3**teams worked with

**4**home-lab builds

**10+**protocols and services

## \~/about

I’m a network engineer with hands-on experience in routing, switching, satellite and terrestrial infrastructure, and network automation with Python. I configure and troubleshoot Cisco, Nivetti and Tejas MPLS-TP devices, with solid fundamentals in BGP, OSPF, EIGRP, VLANs, VPNs and IPv4/IPv6.

Outside of work I build Linux lab infrastructure: self-hosted collaboration platforms, custom Linux ISO images and one-way data transfer systems.

### Right now

- Maintaining internal network labs at WESEE.
- Supporting developers on Indian Navy projects.

### Looking for

- Large-scale, reliable network systems.
- Work close to the hardware and the command line.

## \~/skills

networking

LAN/WANTCP/IPBGPOSPFEIGRPIPv4/IPv6VLANsVPNsOpenVPNVAPT resolution

services

DNSDHCPFTPHTTP/HTTPSSSHHSRPVRRPTCP/UDP

hardware

Cisco routers and switchesNivetti routersTejas MPLS-TPFirewalls

linux

Linux administrationVMware WorkstationCustom ISO buildsNextcloudGitea

tools

Tejas NMS/EMSGNS3Packet TracerInfraon NMSGrafanaWiresharkBlueCoatJovianPuTTY

automation

PythonNetwork scriptingAPI-based automation

## \~/experience

Sept 2025 –\
present

### Assistant Developer, WESEE (Indian Navy)

Jangoo Technologies

- Contribute to networking and development work for WESEE, a technical establishment under the Indian Navy.
- Maintain internal network labs and assist developers with project implementation.
- Connect networking requirements to development tasks.

Mar 2025 –\
Sept 2025

### Network Engineer

Hughes Communication India Limited (via KMG Tech Solution Pvt. Ltd.)

- Configured, maintained and troubleshot VSAT and terrestrial network infrastructure.
- Monitored performance with Grafana, BlueCoat and Jovian, and analyzed signal attenuation.
- Worked with cross-functional teams to deploy satellite communication solutions for enterprise clients.

Sept 2024 –\
Mar 2025

### Apprentice, PowerGrid Corporation of India Limited

NEC Corporation of India

- Helped the NOC team configure and deploy Nivetti routers and Tejas MPLS-TP1400/1600 devices.
- Supported ground teams in setting up telecom networks to specification.
- Talked with clients to troubleshoot issues and deliver timely fixes.

## \~/projects

### Data diode: one-way transfer

Linux · Networking · Python

- Enforces one-way flow between isolated network segments, mirroring air-gapped transfer needs.
- Blocks return-path traffic at host and network level, verified end to end.
- Scripted validation and logging check data integrity.

### Self-hosted Nextcloud and Gitea

Linux · Docker/VM · Nextcloud · Gitea

- File sync and Git hosting on a local network for lab projects.
- Static addressing, reverse proxy and access rules so LAN clients can reach both.
- Managed users, storage and basic backups.

### Custom Linux ISO

Linux · ISO remastering · Shell

- Autologin and automatic root session on boot.
- Rebuilt after changing boot and init configuration; tested on VMs and physical hardware.
- Cut setup time on repeated lab rebuilds.

## \~/labs

Hands-on builds from my own network lab. Pick one to see the setup, what I built and how it was checked.

### One-way link, live demo

Simplified illustration of the idea, not my project code.

Network A\
source

Network B\
isolated

Pick a direction.

### What I built

- A data diode that enforces one-way flow between isolated network segments.
- Host-level and network-level controls that restrict return-path traffic.

#### How I checked it

- Verified one-way transfer end to end.
- Scripted validation and logging for data integrity and reliability.

#### Stack

LinuxNetworkingPython

### Lab network layout

Request path from a LAN client to each service.

LAN clients

→

Reverse proxy\
access rules

→

Nextcloud

Gitea

Both services run on static IP addresses inside the local network.

### What I built

- Nextcloud for file sync and collaboration, and Gitea for Git version control, for lab projects.
- Static addressing plus reverse proxy and access rules so both are reachable from LAN clients.

#### Day-to-day running

- User access management.
- Storage and basic backup and maintenance.

#### Stack

LinuxDocker/VMNextcloudGitea

### Remaster pipeline

Unpack\
ISO

→

Edit boot\
and init

→

Rebuild\
image

→

Test VM\
and hardware

Typical remaster workflow. Exact paths and tools vary by distro.

```
mkdir -p iso && sudo mount -o loop distro.iso /mnt
cp -a /mnt/. iso/ && sudo umount /mnt
# edit boot/init config for autologin
xorriso -as mkisofs -o custom.iso \
  -b isolinux/isolinux.bin -c isolinux/boot.cat \
  -no-emul-boot -boot-load-size 4 -boot-info-table iso/
```

### What I built

- A modified Linux ISO that logs in automatically and starts a root session on boot.
- Rebuilt and repackaged the image after changing boot and init configuration.

#### Why it helps

- Faster lab deployment and testing.
- Less manual setup on repeated rebuilds during networking experiments.

#### Validated on

Virtual machinesPhysical test hardware

### Config snippets

Illustrative Cisco IOS examples with documentation IP addresses, not real device configs.

```

```

### Then verify

The first command to run after applying the config:

```

```

#### Related experience

- Configuring and troubleshooting Cisco, Nivetti and Tejas MPLS-TP devices.
- Routing fundamentals: BGP, OSPF, EIGRP, VLANs, VPNs, IPv4/IPv6.

### Secure tunnel across two ISPs

Two systems on different networks and different ISPs, joined by an OpenVPN tunnel.

System A\
secure network\
ISP 1

System B\
unsecure network\
ISP 2

Encrypted OpenVPN tunnel over the internet

#### Typical client config (illustrative)

```
client
dev tun
proto udp
remote vpn.example.com 1194
ca ca.crt
cert client.crt
key client.key
cipher AES-256-GCM
verb 3
```

### What I built

- A remote connection between two systems on different networks and different ISPs, using the OpenVPN application.
- A secure tunnel between a secure network and an unsecure network, so traffic crosses the untrusted path encrypted.

#### Typical checks (illustrative)

- Tunnel interface is up on both systems.
- Each system can ping the other’s tunnel IP.
- Traffic to the remote network goes through the tunnel.

#### Stack

OpenVPNNetworkingSecure tunneling

## \~/education

### B.Tech, Computer Science and Engineering

ITM University, Gwalior\
GPA 7.3/10 · Aug 2019 – May 2023

### Certifications

Industrial Training in CCNA (Routing and Switching), Network Bulls\
Internship Certificate, NEC Corporation of India

## \~/contact

[linkedin.com/in/grv-pal1812](https://linkedin.com/in/grv-pal1812)

© 2026 Gaurav Kumar Pal