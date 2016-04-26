## How to avoid giving sudo every time, go inside sudo mode
  sudo -s
  
## system startup script running and disabling

#### To start a daemon at startup:
  update-rc.d service_name defaults
  
#### To remove:
  update-rc.d -f service_name remove


