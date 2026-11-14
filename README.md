# NOMADIC SHOP — GitHub Pages Demo Storefront

A static fashion storefront built with HTML5, CSS3 and vanilla JavaScript. It includes 69 demo products, category browsing, search, filters, product details, local cart, wishlist, demo checkout, order history/tracking in the same browser, and informational pages.

## Run locally

Because the project loads local assets and data, run it through a local static web server (recommended) rather than opening files directly. For example, with Python installed, open a terminal in this folder and run `python -m http.server 8000`, then visit `http://localhost:8000`. No build step is required.

## Deploy to GitHub Pages

1. Create a GitHub repository.
2. Upload the contents of this folder to the repository root (including `.nojekyll`).
3. Open **Settings → Pages**.
4. Select **Deploy from a branch**, choose `main` and `/ (root)`, then Save.
5. Wait for GitHub Pages to publish and open the URL shown there.

All internal links and asset paths are relative, so the project supports repository subpaths.

## Demo-only limitations — read before publishing

- Cart, wishlist, demo account, newsletter, contact enquiries and orders are stored in the visitor's browser LocalStorage. They are not sent to a shop owner and do not sync across devices.
- LocalStorage authentication is not secure. Do not use real passwords or sensitive personal/payment data.
- Checkout is a demonstration only. No real bKash, Nagad, card, bank or Cash-on-Delivery order is transmitted or charged. A real shop requires a secure backend, database, order management and payment gateway integration.
- Product images currently consist of original SVG illustrations, not authentic product photography. Replace them with properly licensed product photos before commercial launch.
- Configure verified business contact details, delivery terms, policies, social accounts, product stock and prices before publishing.
- Customer reviews and ratings are sample/demo content, not verified buyer reviews.

## Project checks

JavaScript syntax and local asset references were checked for this delivery. Browser-level testing on GitHub Pages and real payment processing are not represented as completed.
