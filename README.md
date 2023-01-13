### Python script to automate transferring build files via SFTP to remote HYCU backup controller 

### TODO:
- [ ] Check if paramiko library is more suitable
- [ ] SCRIPT PROBABLY DOESN'T WORK IF REMOTE HOST IS NOT IN THE known_hosts file (see if it's possible to edit the file via the script)
- [ ] Copy files from local Virtual Appliance folder (Use either pysftp or os module)
- [ ] Replace the files in remote
- [ ] Add possible parameters
- [ ] Handle password security
- [ ] Handle all checks for file.exists and exceptions