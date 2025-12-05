# pdf-tool
Simple self-hosted web application to edit pdf files I build to practice and have fun. Also, many pdf-arranger I found are "free", with ads or lots of cookies, or for desktop-only. So I made my own software to manage PDFs and it's hosted on my home lab.

The development is still at the very beginning, but I aim to implement all the more useful features, such as split documents, merge, delete pages and more. 

## Startup
The easiest way to start this application is by using docker compose, running:
```
docker compose up -d
```

Alternatively, you can start manually the backend and the frontend.
- Backend: 
```
cd pdf-tool/pdf-tool-backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Frontend: 
```
cd pdf-tool/pdf-tool-frontend
npm run dev -- --open
```
Later I'm going to add also a systemd daemon and a configuration script.

## Security notes
This is NOT currently safe to host openly on the internet, so it is strongly suggested to access the app through a vpn, such as wireguard. In my other repo, `SuperT457/scripts` there is a basic configuration file for that. 