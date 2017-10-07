
# Flask Firebase REST API

This application includes a is a sample Flask app that uses firebase db
Data is loaded from a cvs file to firebase
The purpose of the app is to CRUD this data through an API
Before we begin, you need a firebase account. Then you need to create a project -find this [in the console here](https://console.firebase.google.com). Then we need to collect all the config values we need to run the application:


 
You can find all these values, going to your project, then to Authentication on the left side menu (as of october 2017 console interface)
and on the top right you should see a 'WEB SETUP' button. There you will find all these values

 
 | Config&nbsp;Value  | Description |
 | :-------------  |:------------- |
ApiKey | Your primary Firebase project  identifier - (https://console.firebase.google.com/u/0/YOURPROJECTID/settings/general).
AuthDomain | Used to authenticate.
DatabaseURL | The url to access your database.
StorageBucke | We might need not need this (as of the first objective[simple api crud]), but if you want to follow along, please copy this too.

## Setting Up The Python Application

This application uses the lightweight [Flask Framework](http://flask.pocoo.org/).

### Mac & Linux

Begin by creating a configuration file for your application:

```bash
cp .env.example .env
```

Edit `.env` with the four configuration parameters we gathered from above. Export
the configuration in this file as system environment variables like so on Unix
based systems:

```bash
source .env
```

### Windows (PowerShell)

Begin by creating a configuration file for your application:

```powershell
cp .env.example.ps1 .env.ps1
```

Edit `.env.ps1` with the four configuration parameters we gathered from above.
"Dot-source" the file in PowerShell like so:

```powershell
. .\.env.ps1
```

This assumes you will run the application in the same PowerShell session. If not,
edit the `.env.ps1` and uncomment the `[Environment]::SetEnvironmentVariable` calls.
After re-running the script, the environment variables will be peramently set for
your user account.

## All Platforms

Note: It's better if you do it on a virtual environment
Next, we need to install our depenedencies:

```bash
pip install -r requirements.txt
```

Run the load_catalog using the `python` command.

```bash
python load_catalog.py
```

Run the application using the `python` command.

```bash
python app.py
```

Your application should now be running at http://localhost:5000.

There's just a few more steps to get to your server. You have two options here

##Option 1

1. [Download and install ngrok](https://ngrok.com/download)

2. Run ngrok :

    ```bash
    ngrok http 5000
    ```

3. When ngrok starts up, it will assign a unique URL to your tunnel.
It might be something like `https://asdf456.ngrok.io`. Take note of this.


You should now be ready to go testing the API!
Next: Authentication and front-end



##Option 2

1. Deploy on Heroku


## License

MIT
