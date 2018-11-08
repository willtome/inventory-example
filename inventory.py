#!/usr/bin/env python


import yaml
import json

def read_file(site):

  with open("sites/"+site+".yml", 'r') as stream:
      try:
          return  yaml.load(stream)
      except yaml.YAMLError as exc:
          print(exc)

# env
# site
# node_type
# coordinates

def main():
  site = 'boston'
  env = 'production'
  inventory_in = read_file(site)
  inventory_out = {}
  inventory_out['environment_' + env] = { 'hosts': [] }
  inventory_out['site_' + site] = { 'hosts': [], 'vars': { 'coordinates': inventory_in['coordinates']} }
  inventory_out['node_type_directors'] = { 'hosts': [] }
  inventory_out['node_type_controllers'] = { 'hosts': [] }
  for key in inventory_in:
    
    if key == 'directors':
      inventory_out['node_type_directors']['hosts'].append(inventory_in[key])
      inventory_out['environment_' + env]['hosts'].append(inventory_in[key])
      inventory_out['site_' + site]['hosts'].append(inventory_in[key])    

    if key == 'controllers':
      for item in inventory_in['controllers']:
        inventory_out['node_type_controllers']['hosts'].append(item)  
        inventory_out['environment_' + env]['hosts'].append(item)
        inventory_out['site_' + site]['hosts'].append(item)    
 
  #print(inventory_in)
  #print(inventory_out)
  print(json.dumps(inventory_out))
  

if __name__ == '__main__':
    main()
