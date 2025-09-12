from market import app, db
from market.models import Item

items = [
    {
        "name": "MacBook Pro 16",
        "price": 2400,
        "barcode": "111222333444",
        "description": "Apple MacBook Pro 16-inch with M2 Pro chip, 16GB RAM, 1TB SSD.",
        "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
    },
    {
        "name": "Dell XPS 15",
        "price": 1900,
        "barcode": "222333444555",
        "description": "Dell XPS 15 with Intel i7, 16GB RAM, 512GB SSD, InfinityEdge Display.",
        "image_url": "https://images.unsplash.com/photo-1587202372775-98927a7d89a6"
    },
    {
        "name": "iPhone 15 Pro Max",
        "price": 1500,
        "barcode": "333444555666",
        "description": "Apple iPhone 15 Pro Max with A17 Pro chip, Titanium build, 256GB storage.",
        "image_url": "https://images.unsplash.com/photo-1695048139975-f3e04dc3d6a6"
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "price": 1400,
        "barcode": "444555666777",
        "description": "Samsung Galaxy S24 Ultra with Snapdragon 8 Gen 3, 12GB RAM, 200MP camera.",
        "image_url": "https://images.unsplash.com/photo-1611587266516-8b69b87d6eaf"
    },
    {
        "name": "Sony Alpha A7 IV",
        "price": 2800,
        "barcode": "555666777888",
        "description": "Sony Alpha A7 IV full-frame mirrorless camera with 33MP sensor.",
        "image_url": "https://images.unsplash.com/photo-1519183071298-a2962be90b8e"
    },
    {
        "name": "Canon EOS R5",
        "price": 3900,
        "barcode": "666777888999",
        "description": "Canon EOS R5 professional mirrorless camera with 45MP sensor and 8K video.",
        "image_url": "https://images.unsplash.com/photo-1519181245277-cffeb31da2a5"
    },
    {
        "name": "Rolex Submariner",
        "price": 15000,
        "barcode": "777888999000",
        "description": "Rolex Submariner Date luxury Swiss watch with automatic movement.",
        "image_url": "https://images.unsplash.com/photo-1524805444758-089113d48a6d"
    },
    {
        "name": "BMW X5",
        "price": 60000,
        "barcode": "888999000111",
        "description": "BMW X5 xDrive40i SUV with luxury interior and advanced tech features.",
        "image_url": "https://images.unsplash.com/photo-1616787749515-28a1b9230eaf"
    },
    {
        "name": "Tesla Model S",
        "price": 90000,
        "barcode": "999000111222",
        "description": "Tesla Model S Plaid with electric powertrain, 0-60 mph in 1.9 seconds.",
        "image_url": "https://images.unsplash.com/photo-1502877338535-766e1452684a"
    },
    {
        "name": "PlayStation 5",
        "price": 700,
        "barcode": "000111222333",
        "description": "Sony PlayStation 5 next-gen gaming console with DualSense controller.",
        "image_url": "https://images.unsplash.com/photo-1606813907291-5cf0ee3c2a3f"
    },
    {
        "name": "DJI Mavic 3",
        "price": 2200,
        "barcode": "111222333555",
        "description": "DJI Mavic 3 professional drone with 4/3 CMOS Hasselblad camera.",
        "image_url": "https://images.unsplash.com/photo-1508610048659-a06b669e9d17"
    }
]

def seed_items():
    with app.app_context():  # ✅ FIXED
        for item in items:
            existing_item = Item.query.filter_by(name=item["name"]).first()
            if not existing_item:
                new_item = Item(
                    name=item["name"],
                    price=item["price"],
                    barcode=item["barcode"],
                    description=item["description"],
                    image_url=item["image_url"]
                )
                db.session.add(new_item)
        db.session.commit()
        print("✅ Items seeded successfully!")

if __name__ == "__main__":
    seed_items()
