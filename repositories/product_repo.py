from schemas.product import Product, UseCase
from rapidfuzz import fuzz, process, utils


class ProductRepo:
    _cameras: dict[int, Product] = {
        # Wildlife photography
        1: Product(
            id=1,
            name="Falconer X9",
            description=(
                "Flagship mirrorless camera built for wildlife photography. Combines a high-resolution "
                "sensor with fast animal and bird eye-tracking autofocus, so you can crop deep into a "
                "frame and still keep detail. Fully weather sealed for long days in the field."
            ),
            pros=[
                "Animal and bird eye-detection autofocus locks on even through branches",
                "High resolution leaves plenty of room to crop distant subjects",
                "Fully weather sealed against rain, dust and freezing temperatures",
                "Long battery life suited to all-day outings",
                "Fast 30 fps burst for birds in flight",
            ],
            cons=[
                "Expensive body before adding long telephoto lenses",
                "Heavy once paired with a super-telephoto lens",
                "Large 60MP files fill memory cards and slow down editing",
            ],
            use_case="wildlife photography",
            specification={
                "best_for": "wildlife, birds in flight",
                "camera_type": "mirrorless",
                "sensor": "full frame",
                "resolution": "60 MP",
                "max_burst_fps": "30",
                "autofocus": "animal/bird eye detection, 759 points",
                "image_stabilization": "in-body, 8 stops",
                "weather_sealing": "full",
                "battery_life_shots": "800",
                "weight_g": "740",
                "video": "8K 30fps",
            },
            price=4299.00,
        ),
        2: Product(
            id=2,
            name="Trailhawk R5",
            description=(
                "Lightweight crop-sensor camera for hobbyist wildlife and nature photographers. The APS-C "
                "sensor gives extra reach from any lens, so you can photograph distant animals with "
                "smaller, cheaper telephoto lenses. Easy to carry on long hikes."
            ),
            pros=[
                "APS-C crop factor (1.5x) adds reach from the same lens",
                "Light and compact for hiking and travel",
                "Animal-detection autofocus at an entry-level price",
                "Weather resistant for light rain and dust",
                "Affordable entry into wildlife photography",
            ],
            cons=[
                "Weaker low-light performance at dawn and dusk",
                "Smaller buffer fills quickly during long bursts",
                "Weather resistance is partial, not full sealing",
            ],
            use_case="wildlife photography",
            specification={
                "best_for": "beginner/hobbyist wildlife, nature hikes",
                "camera_type": "mirrorless",
                "sensor": "APS-C (1.5x crop)",
                "resolution": "32 MP",
                "max_burst_fps": "15",
                "autofocus": "animal eye detection, 425 points",
                "image_stabilization": "in-body, 5 stops",
                "weather_sealing": "partial",
                "battery_life_shots": "550",
                "weight_g": "510",
                "video": "4K 60fps",
            },
            price=1399.00,
        ),
        # People portraits
        3: Product(
            id=3,
            name="Lumière P1",
            description=(
                "Portrait-focused full frame camera tuned for natural skin tones and smooth background "
                "blur. Human eye-detection autofocus keeps the eye sharp at wide apertures, and the "
                "high dynamic range sensor handles bright windows and studio lighting alike."
            ),
            pros=[
                "Very accurate, flattering skin tone color science",
                "Reliable human eye autofocus at f/1.2 apertures",
                "Wide dynamic range keeps highlights and shadows in backlit portraits",
                "Excellent low-light image quality for indoor sessions",
                "Tilting touchscreen for low and high angles",
            ],
            cons=[
                "Slow 8 fps burst is not suited to action",
                "Little weather sealing for outdoor use in bad weather",
                "Native portrait lenses are expensive",
            ],
            use_case="portrait photography",
            specification={
                "best_for": "studio and natural-light portraits, weddings",
                "camera_type": "mirrorless",
                "sensor": "full frame",
                "resolution": "45 MP",
                "max_burst_fps": "8",
                "autofocus": "human face/eye detection, 693 points",
                "image_stabilization": "in-body, 7 stops",
                "weather_sealing": "minimal",
                "battery_life_shots": "600",
                "weight_g": "650",
                "video": "4K 30fps",
            },
            price=2799.00,
        ),
        4: Product(
            id=4,
            name="Candid C2",
            description=(
                "Compact fixed-lens camera for street and everyday portraits. A bright 35mm f/1.4 lens "
                "and quiet shutter let you photograph people without being intrusive, and the small size "
                "makes subjects feel relaxed in front of the camera."
            ),
            pros=[
                "Bright f/1.4 lens gives soft background blur",
                "Silent leaf shutter for discreet candid shots",
                "Pocketable size makes subjects more relaxed",
                "Built-in film-style color profiles",
                "Lower cost than a body plus portrait lens",
            ],
            cons=[
                "Fixed 35mm lens cannot zoom or be swapped",
                "Smaller APS-C sensor gives less blur than full frame",
                "Short battery life",
            ],
            use_case="portrait photography",
            specification={
                "best_for": "street, candid and everyday portraits",
                "camera_type": "compact (fixed lens)",
                "sensor": "APS-C",
                "resolution": "26 MP",
                "max_burst_fps": "11",
                "autofocus": "human face/eye detection, 117 points",
                "image_stabilization": "none",
                "weather_sealing": "minimal",
                "battery_life_shots": "380",
                "weight_g": "420",
                "video": "4K 30fps",
                "lens": "35mm equivalent f/1.4 fixed",
            },
            price=1599.00,
        ),
        # Sports
        5: Product(
            id=5,
            name="Velocity S1 Pro",
            description=(
                "Professional sports camera built for speed. The stacked sensor captures 40 fps with no "
                "blackout, and the AI tracking autofocus follows players across the frame. A rugged body "
                "and dual card slots hold up to stadium and sideline work."
            ),
            pros=[
                "40 fps blackout-free burst never misses the decisive moment",
                "Subject-tracking AF follows players, balls and vehicles",
                "Huge buffer for long continuous sequences",
                "Rugged, fully sealed body with dual card slots",
                "Built-in ethernet for fast transfer to editors",
            ],
            cons=[
                "Very expensive and aimed at professionals",
                "24MP leaves less room to crop than high-res bodies",
                "Large, heavy body with an integrated grip",
            ],
            use_case="action photography",
            specification={
                "best_for": "professional sports, fast action",
                "camera_type": "mirrorless",
                "sensor": "full frame stacked",
                "resolution": "24 MP",
                "max_burst_fps": "40",
                "autofocus": "AI subject tracking (people, vehicles, balls), 1053 points",
                "image_stabilization": "in-body, 6 stops",
                "weather_sealing": "full",
                "battery_life_shots": "1500",
                "weight_g": "1100",
                "video": "6K 60fps",
            },
            price=5999.00,
        ),
        6: Product(
            id=6,
            name="Sprint A6",
            description=(
                "Affordable action camera for parents, amateur sports and school events. Fast burst and "
                "tracking autofocus make it easy to capture moving kids and players, at a price far "
                "below professional sports bodies."
            ),
            pros=[
                "Fast 20 fps burst at a mid-range price",
                "Tracking autofocus is easy for beginners to use",
                "APS-C crop adds reach from the sidelines",
                "Light enough to carry all day at tournaments",
                "Good battery life for long game days",
            ],
            cons=[
                "Struggles in dim indoor gyms and night games",
                "Electronic viewfinder lags slightly during fast bursts",
                "Only one card slot",
            ],
            use_case="action photography",
            specification={
                "best_for": "amateur sports, kids' games, school events",
                "camera_type": "mirrorless",
                "sensor": "APS-C (1.5x crop)",
                "resolution": "26 MP",
                "max_burst_fps": "20",
                "autofocus": "subject tracking (people), 425 points",
                "image_stabilization": "in-body, 5 stops",
                "weather_sealing": "partial",
                "battery_life_shots": "700",
                "weight_g": "560",
                "video": "4K 60fps",
            },
            price=1199.00,
        ),
    }

    _cameras_by_name: dict[str, Product] = {
        camera.name: camera for camera in _cameras.values()
    }

    def get_product_by_id(self, id: int) -> Product | None:
        return self._cameras[id]

    def get_product_by_name(self, name: str) -> Product:
        cameras = list(self._cameras_by_name.keys())
        best_match = process.extractOne(
            name,
            cameras,
            scorer=fuzz.WRatio,
            processor=utils.default_process
        )
        return self._cameras_by_name[best_match[0]]

    def get_products_by_use_case(self, use_case: UseCase) -> list[Product]:
        cameras: list[Product] = []
        for k, v in self._cameras.items():
            if v.use_case == use_case:
                cameras.append(v)
        return cameras
