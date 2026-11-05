import os
import urllib.request

# Create images directory
os.makedirs("images", exist_ok=True)

# Image URLs matching each exact product category
images = {
    # Core Banners & Logo
    "logo.png": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Apple-Dark.svg",  # your logo
    "banner-notice.png": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=700",
    "banner-msg.png": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=350",
    "banner-service.png": "https://images.unsplash.com/photo-1581092921461-eab62e97a780?w=350",
    "affiliations.png": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=250",
    # Flash Sale
    "flash-1-tv.jpg": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400",
    "flash-2-gpu.jpg": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=400",
    "flash-3-camera.jpg": "https://images.unsplash.com/photo-1557597774-9d273605dfa9?w=400",
    "flash-4-ptz.jpg": "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400",
    "flash-5-yoga.jpg": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400",
    "flash-6-loq.jpg": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400",
    # Featured Products
    "feat-1-pc.jpg": "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?w=400",
    "feat-2-pc.jpg": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=400",
    "feat-3-pc.jpg": "https://images.unsplash.com/photo-1547082299-de196ea013d6?w=400",
    "feat-4-pc.jpg": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400",
    "feat-5-gpu.jpg": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=400",
    "feat-6-gpu.jpg": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=400",
    # Latest Products
    "latest-1-monitor.jpg": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400",
    "latest-2-monitor.jpg": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400",
    "latest-3-monitor.jpg": "https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=400",
    "latest-4-minipc.jpg": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=400",
    "latest-5-speaker.jpg": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=400",
    "latest-6-monitor.jpg": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400",
    # Best Sellers
    "best-1-monitor.jpg": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400",
    "best-2-ram.jpg": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=400",
    "best-3-gpu.jpg": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=400",
    "best-4-monitor.jpg": "https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=400",
    "best-5-gpu.jpg": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=400",
    "best-6-monitor.jpg": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400",
}

print("Downloading images into 'images/' folder...")
for filename, url in images.items():
  filepath = os.path.join("images", filename)
  if not os.path.exists(filepath):
    urllib.request.urlretrieve(url, filepath)
    print(f"✓ Saved: {filename}")
print("All images are ready in 'images/' folder!")
