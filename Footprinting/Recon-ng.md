# Recon-ng

Recon-ng is a Python-based framework that offers users automated network reconnaissance and information gathering. Its interface is similar to Metasploit and relies on various modules for functionality. Some modules require an API key, but the website for obtaining these keys is currently down.

## Intallation

- Recon-ng comes pre-installed on Kali Linux. For other Linux distributions, you can install it using:

```bash
apt-get install recon-ng
```

## Basic Usage

- To start Recon-ng:

```bash
recon-ng 
```
## Key Features

### Workspaces:

Recon-ng allows working with different workspaces:
- List workspaces: `workspaces list`
- Create workspace: `workspaces create [Name]`
- Load workspace: `workspaces load [Name]`
- Remove workspace: `workspaces remove [Name]`

### Database Management:

- View database schema: `db schema`
- Delete information: `db delete [information]`
- Insert domain: `db insert domains`

### Viewing Stored Information:

`show [information type]`

- Examples: show hosts, show domains, show credentials


### Snapshots:
- Create snapshot: `snapshot take`
- Remove snapshot: `snapshot remove [name]`
- List snapshots: `snapshots list`
- Load snapshot: `snapshot load [name]`

### Modules:
- List marketplace tools: marketplace search
- Focused search: `marketplace search [keyword]`
- Install module: `marketplace install [path]`
- Install all modules: `marketplace install all`
- Load module: `modules load [module]`
- List module options: `options list`
- Set module option: `options set [field] [value]`
- Run module: `run`
- Exit module: `back`

### API Keys
- Add API key: keys add [api_name] [key]
- List keys: keys list
- Remove key: keys remove [api_name]
