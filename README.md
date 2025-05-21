# steam_link_desktop

A Python script packaged as a Windows application can turn your Steam Link into a remote desktop software. In my tests, it has significantly lower latency compared to Tailscale+Moonlight, and RealVNC, even across oceans.

It launch the system default browser in full-screen mode on Windows, then minimize it while keeping the browser process alive. This ensures Steam Link (Remote Play) maintains the stream without disconnecting, effectively mimicking a "game-like" full-screen placeholder.

I discovered this by accident. Tailscale+Moonlight has very high latency when the distance between two devices is very far, and even when I set up my own derp server, the latency is still very high. However, the effect of Steam Link is unexpectedly good, so I wanted to run Epic Games on Steam Link. When I closed the game, I found that the desktop was still open. I then realized that when I opened the game, the Epic Games login was triggered. The login triggered the browser to go full screen. When I minimized the browser, the desktop remained. So, here is the result🤣

Download the exe file and open add that to your steam!

Haven't tested on Linux, I will update for linux later if it work, lack of time right now.
