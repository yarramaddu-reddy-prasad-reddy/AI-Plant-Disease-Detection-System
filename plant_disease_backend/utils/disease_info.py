# utils/disease_info.py

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "description": "Apple scab is a fungal disease caused by Venturia inaequalis that creates dark, olive-colored lesions on leaves and scabby spots on fruit.",
        "treatment": "Remove and destroy fallen infected leaves. Apply copper-based fungicides or synthetic fungicides like Captan or Mancozeb.",
        "prevention": "Plant scab-resistant cultivars, prune trees to increase air circulation, and avoid overhead irrigation.",
        "pesticide": "Captan 50 WP, Mancozeb, or Myclobutanil",
        "organic": "Neem Oil, Liquid Copper Spray, or Potassium Bicarbonate",
        "watering": "Drip irrigate at the soil level; avoid wetting tree leaves.",
        "fertilizer": "Use a balanced NPK fertilizer. Avoid excessive nitrogen late in the season.",
        "severity": "Medium"
    },
    "Apple___Black_rot": {
        "description": "Black rot causes leaf spots (frogeye leaf spot), fruit rot with concentric rings, and cankers on branches.",
        "treatment": "Prune out dead wood, cankers, and mummified fruit during winter. Spray Captan or sulfur-based fungicides during bloom.",
        "prevention": "Remove dead wood from nearby trees and keep the orchard orchard sanitation high.",
        "pesticide": "Captan, Thiophanate-methyl",
        "organic": "Copper Sprays or Sulfur-based sprays",
        "watering": "Water at the root zone; keep tree canopy clean and dry.",
        "fertilizer": "Balanced NPK (10-10-10) in early spring.",
        "severity": "High"
    },
    "Apple___Cedar_apple_rust": {
        "description": "Fungal disease requiring two hosts (apple and eastern red cedar). Causes bright orange-yellow spots on apple leaves.",
        "treatment": "Apply systemic fungicides like Myclobutanil when flower buds open in spring.",
        "prevention": "Remove nearby eastern red cedar trees if possible, or plant resistant apple varieties.",
        "pesticide": "Myclobutanil or Immunox",
        "organic": "Sulfur sprays or Copper soaps",
        "watering": "Standard root watering; avoid wetting foliage.",
        "fertilizer": "Standard balanced fertilizer.",
        "severity": "Medium"
    },
    "Apple___healthy": {
        "description": "The apple foliage and fruit appear healthy with no signs of fungal or bacterial infection.",
        "treatment": "None required.",
        "prevention": "Maintain proper pruning, adequate sunlight, and routine monitoring.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Maintain regular watering schedule based on weather.",
        "fertilizer": "Balanced NPK organic compost or fertilizer annually.",
        "severity": "None"
    },
    "Blueberry___healthy": {
        "description": "The blueberry plant leaves and stems show vigorous growth without visible disease symptoms.",
        "treatment": "None required.",
        "prevention": "Maintain soil pH between 4.5 and 5.5 and mulch with pine bark.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Keep soil consistently moist with acidic water.",
        "fertilizer": "Acid-forming fertilizer like ammonium sulfate.",
        "severity": "None"
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "Fungal growth causing white, powdery patches on leaves and shoots, curling young leaves upward.",
        "treatment": "Apply sulfur or potassium bicarbonate sprays early in the infection cycle.",
        "prevention": "Prune interior branches to increase sunlight and air movement through the tree canopy.",
        "pesticide": "Myclobutanil or Propiconazole",
        "organic": "Potassium Bicarbonate or Neem Oil",
        "watering": "Water soil directly in early morning hours.",
        "fertilizer": "Balanced fruit tree fertilizer.",
        "severity": "Medium"
    },
    "Cherry_(including_sour)___healthy": {
        "description": "Cherry foliage is green, clean, and functioning properly.",
        "treatment": "None required.",
        "prevention": "Keep canopy pruned and clear ground debris in winter.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Regular irrigation during fruit development.",
        "fertilizer": "Standard tree fertilizer in early spring.",
        "severity": "None"
    },
    "Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot": {
        "description": "Causes rectangular, tan-to-gray lesions running parallel to leaf veins, reducing photosynthesis drastically.",
        "treatment": "Apply foliar fungicides like strobilurins or triazoles if infection occurs early in the season.",
        "prevention": "Rotate crops with non-grass species and plant resistant corn hybrids.",
        "pesticide": "Azoxystrobin or Pyraclostrobin",
        "organic": "Copper-based fungicides",
        "watering": "Avoid overhead spray; use furrow or drip systems.",
        "fertilizer": "Sufficient nitrogen according to soil tests.",
        "severity": "High"
    },
    "Corn_(maize)___Common_rust_": {
        "description": "Fungal rust characterized by oval-to-elongated cinnamon-brown pustules on both upper and lower leaf surfaces.",
        "treatment": "Fungicide sprays are rarely economic unless severe early-season infection hits susceptible hybrids.",
        "prevention": "Plant rust-resistant hybrids and practice crop rotation.",
        "pesticide": "Mancozeb or Azoxystrobin",
        "organic": "Sulfur-based sprays",
        "watering": "Maintain normal field irrigation.",
        "fertilizer": "Balanced nitrogen and potassium.",
        "severity": "Medium"
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "Fungal disease causing large, cigar-shaped gray-green or tan lesions on leaves.",
        "treatment": "Apply foliar fungicides at tasseling stage if disease pressure is high.",
        "prevention": "Till residue under to accelerate decomposition and rotate crops annually.",
        "pesticide": "Propiconazole or Pyraclostrobin",
        "organic": "Bio-fungicides like Bacillus subtilis",
        "watering": "Avoid overhead sprinkler systems if possible.",
        "fertilizer": "Balanced NPK application.",
        "severity": "High"
    },
    "Corn_(maize)___healthy": {
        "description": "Corn leaves are dark green and vibrant without spots, blights, or rusts.",
        "treatment": "None required.",
        "prevention": "Maintain proper crop management and crop rotation.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Ensure adequate moisture during silk and tassel development.",
        "fertilizer": "Nitrogen-rich crop fertilizer.",
        "severity": "None"
    },
    "Grape___Black_rot": {
        "description": "Fungal infection causing reddish-brown spots on leaves and transforming grape berries into hard, black, shriveled mummies.",
        "treatment": "Spray fungicides like Myclobutanil or Captan starting at bud break.",
        "prevention": "Destroy all mummified fruit and prune vines for maximum airflow.",
        "pesticide": "Myclobutanil, Mancozeb, or Ziram",
        "organic": "Copper Octanoate or Sulfur",
        "watering": "Water drip system near vine trunk.",
        "fertilizer": "Potassium and balanced vineyard fertilizer.",
        "severity": "High"
    },
    "Grape___Esca_(Black_Measles)": {
        "description": "Complex disease causing 'tiger-stripe' interveinal chlorosis on leaves and spotted berries.",
        "treatment": "No cure exists; prune out infected arms or trunks and protect fresh pruning wounds.",
        "prevention": "Sanitize pruning tools between cuts and avoid large pruning wounds in wet weather.",
        "pesticide": "None effective for cure (wound protectants recommended)",
        "organic": "Trichoderma-based pruning paints",
        "watering": "Avoid water stress on vines.",
        "fertilizer": "Maintain balanced soil nutrients.",
        "severity": "High"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "Causes irregular reddish-brown spots on leaves that turn dark brown with age, leading to premature defoliation.",
        "treatment": "Apply copper fungicides post-harvest or during early leaf symptom stage.",
        "prevention": "Remove fallen leaf litter and ensure adequate vine canopy training.",
        "pesticide": "Mancozeb or Copper Oxychloride",
        "organic": "Copper-based sprays",
        "watering": "Water soil directly.",
        "fertilizer": "Balanced potassium-nitrogen blend.",
        "severity": "Medium"
    },
    "Grape___healthy": {
        "description": "Grape foliage is healthy, showing vibrant green leaves and clean clusters.",
        "treatment": "None required.",
        "prevention": "Routine leaf pulling and canopy training.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Deep, infrequent irrigation.",
        "fertilizer": "Annual organic compost or balanced grape food.",
        "severity": "None"
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "Devastating bacterial disease spread by citrus psyllids, causing blotchy mottle on leaves and small, bitter, lopsided green fruit.",
        "treatment": "No cure. Remove infected trees to prevent spreading to surrounding groves.",
        "prevention": "Control Asian citrus psyllid vector using insecticidal sprays or natural predators.",
        "pesticide": "Imidacloprid (for vector control)",
        "organic": "Horticultural oils or Neem oil (against psyllid insects)",
        "watering": "Ensure adequate soil moisture to reduce tree stress.",
        "fertilizer": "Enhanced foliar nutritional sprays (micronutrients).",
        "severity": "Critical"
    },
    "Peach___Bacterial_spot": {
        "description": "Bacterial pathogen causing small water-soaked spots on leaves that fall out (shot-hole effect) and pitted fruit.",
        "treatment": "Apply copper sprays during dormancy and early bloom.",
        "prevention": "Avoid planting in windblown sandy soils and use resistant cultivars.",
        "pesticide": "Oxytetracycline or Copper Hydroxide",
        "organic": "Copper soap fungicide",
        "watering": "Avoid wetting tree foliage during irrigation.",
        "fertilizer": "Avoid excess nitrogen fertilizer.",
        "severity": "High"
    },
    "Peach___healthy": {
        "description": "Peach tree leaf canopy is dark green with smooth skin and no bacterial lesions.",
        "treatment": "None required.",
        "prevention": "Maintain dormant spraying schedule for preventative maintenance.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Regular fruit-tree drip irrigation.",
        "fertilizer": "Nitrogen-balanced fruit tree fertilizer.",
        "severity": "None"
    },
    "Pepper,_bell___Bacterial_spot": {
        "description": "Bacterial disease causing small, dark, water-soaked spots on leaves and raised scab-like lesions on peppers.",
        "treatment": "Apply fixed copper mixed with Mancozeb to reduce bacterial pressure.",
        "prevention": "Use certified disease-free seeds and practice 2-3 year crop rotation.",
        "pesticide": "Copper Hydroxide + Mancozeb",
        "organic": "Copper octanoate",
        "watering": "Use drip line irrigation instead of sprinklers.",
        "fertilizer": "Balanced tomato/pepper fertilizer.",
        "severity": "High"
    },
    "Pepper,_bell___healthy": {
        "description": "Bell pepper leaves are bright green, firm, and displaying good health.",
        "treatment": "None required.",
        "prevention": "Maintain weed-free soil and balanced watering.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Deep weekly drip watering.",
        "fertilizer": "Calcium and magnesium-rich plant food.",
        "severity": "None"
    },
    "Potato___Early_blight": {
        "description": "Fungal infection caused by Alternaria solani, characterized by dark brown spots with dark concentric rings ('target' appearance).",
        "treatment": "Apply protective fungicides like Chlorothalonil or Mancozeb.",
        "prevention": "Rotate crops every 2 years and ensure good foliage drying conditions.",
        "pesticide": "Chlorothalonil, Mancozeb",
        "organic": "Copper-based fungicides or Bacillus subtilis",
        "watering": "Irrigate at soil line early in the morning.",
        "fertilizer": "Maintain proper nitrogen and potassium levels.",
        "severity": "Medium"
    },
    "Potato___Late_blight": {
        "description": "Destructive disease caused by Phytophthora infestans, causing pale green to dark water-soaked lesions with white fuzzy mold underneath.",
        "treatment": "Apply systemic fungicides like Ridomil Gold or copper immediately upon detection.",
        "prevention": "Destroy volunteer potato plants and plant certified disease-free seed tubers.",
        "pesticide": "Metalaxyl, Chlorothalonil, Cymoxanil",
        "organic": "Copper Hydroxide",
        "watering": "Avoid over-irrigation; allow soil surface to dry.",
        "fertilizer": "Avoid excess nitrogen late in season.",
        "severity": "Critical"
    },
    "Potato___healthy": {
        "description": "Potato plant leaves are dark green and free from blights or spots.",
        "treatment": "None required.",
        "prevention": "Hill up soil properly around growing stems.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Keep soil evenly moist, especially during tuber setting.",
        "fertilizer": "Potassium-rich potato fertilizer.",
        "severity": "None"
    },
    "Raspberry___healthy": {
        "description": "Raspberry canes and leaves are healthy and vigorous.",
        "treatment": "None required.",
        "prevention": "Prune out spent floricanes after harvest.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Regular drip moisture.",
        "fertilizer": "Balanced berry fertilizer in spring.",
        "severity": "None"
    },
    "Soybean___healthy": {
        "description": "Soybean leaves are clear of rusts, blights, or insect damage.",
        "treatment": "None required.",
        "prevention": "Maintain field crop rotation.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Standard rainfall / center-pivot irrigation.",
        "fertilizer": "Phosphorus and potassium soil replenishment.",
        "severity": "None"
    },
    "Squash___Powdery_mildew": {
        "description": "Fungal disease causing dusty white spots on leaves and stems, causing leaves to yellow and wither prematurely.",
        "treatment": "Spray fungicides like Myclobutanil or sulfur at the first sign of white spots.",
        "prevention": "Space plants generously for air movement and plant mildew-resistant squash varieties.",
        "pesticide": "Myclobutanil or Chlorothalonil",
        "organic": "Neem Oil spray or Potassium Bicarbonate spray",
        "watering": "Water soil at the plant base early in the morning.",
        "fertilizer": "Avoid high nitrogen fertilizers; use balanced organic compost.",
        "severity": "Medium"
    },
    "Strawberry___Leaf_scorch": {
        "description": "Fungal infection causing dark purple leaf spots that enlarge into blotches, leading to scorched leaf edges.",
        "treatment": "Apply fungicides like Captan during early leaf growth.",
        "prevention": "Remove dead strawberry foliage in late winter and avoid dense planting.",
        "pesticide": "Captan or Myclobutanil",
        "organic": "Copper-based fungicide sprays",
        "watering": "Use drip tape beneath strawberry mulch.",
        "fertilizer": "Balanced strawberry fertilizer.",
        "severity": "Medium"
    },
    "Strawberry___healthy": {
        "description": "Strawberry plant foliage is green, clean, and producing runners normally.",
        "treatment": "None required.",
        "prevention": "Replace plants every 3-4 years.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Ensure 1 inch of water weekly.",
        "fertilizer": "Balanced NPK organic fertilizer.",
        "severity": "None"
    },
    "Tomato___Bacterial_spot": {
        "description": "Bacterial pathogen causing dark, water-soaked spots on foliage and raised black specks on fruit.",
        "treatment": "Spray copper combined with Mancozeb.",
        "prevention": "Use seed treatments and rotate crops away from nightshades for 2 years.",
        "pesticide": "Copper Hydroxide + Mancozeb",
        "organic": "Copper Octanoate",
        "watering": "Water at the root base; keep leaves dry.",
        "fertilizer": "Balanced tomato food.",
        "severity": "High"
    },
    "Tomato___Early_blight": {
        "description": "Fungal disease causing brown leaf spots with concentric target-like rings, starting on lower leaves.",
        "treatment": "Apply Chlorothalonil or copper fungicides every 7 to 14 days.",
        "prevention": "Mulch beneath plants to stop soil splashback and remove infected lower leaves.",
        "pesticide": "Chlorothalonil, Mancozeb",
        "organic": "Neem Oil or Copper Fungicide",
        "watering": "Drip irrigation at base.",
        "fertilizer": "Balanced NPK with calcium.",
        "severity": "Medium"
    },
    "Tomato___Late_blight": {
        "description": "Aggressive pathogen causing greasy green-black leaf lesions and rapid plant collapse in humid conditions.",
        "treatment": "Apply protective systemic fungicides immediately upon outbreak warning.",
        "prevention": "Destroy infected plants immediately; do not compost diseased vines.",
        "pesticide": "Chlorothalonil, Cymoxanil",
        "organic": "Copper Fungicide (preventative only)",
        "watering": "Water soil directly.",
        "fertilizer": "Avoid excessive nitrogen.",
        "severity": "Critical"
    },
    "Tomato___Leaf_Mold": {
        "description": "Fungal disease causing pale yellow spots on upper leaf surfaces and velvety olive-green mold underneath.",
        "treatment": "Spray fungicides like Chlorothalonil or copper sulfate.",
        "prevention": "Improve greenhouse/garden ventilation and keep relative humidity below 85%.",
        "pesticide": "Chlorothalonil or Mancozeb",
        "organic": "Copper soap spray",
        "watering": "Drip irrigation early morning.",
        "fertilizer": "Balanced tomato fertilizer.",
        "severity": "Medium"
    },
    "Tomato___Septoria_leaf_spot": {
        "description": "Septoria leaf spot is a fungal disease causing circular spots with dark brown margins and gray centers on lower leaves.",
        "treatment": "Spray Copper Fungicide or Chlorothalonil every 7-10 days upon symptom appearance.",
        "prevention": "Avoid wet foliage, stake tomato plants, and remove infected lower leaves.",
        "pesticide": "Copper Fungicide or Chlorothalonil",
        "organic": "Neem Oil Spray",
        "watering": "Water directly at the base of the plant.",
        "fertilizer": "Potassium-rich fertilizer with adequate calcium.",
        "severity": "High"
    },
    "Tomato___Spider_mites_Two-spotted_spider_mite": {
        "description": "Pest damage caused by microscopic mites that suck plant juices, causing yellow speckling and fine webbing on leaves.",
        "treatment": "Apply insecticidal soap, miticide, or neem oil spray thoroughly on leaf undersides.",
        "prevention": "Keep plants adequately watered; dry, dusty conditions encourage mites.",
        "pesticide": "Abamectin or Bifenthrin",
        "organic": "Insecticidal Soap, Neem Oil, or Predatory Mites",
        "watering": "Avoid plant drought stress.",
        "fertilizer": "Balanced standard fertilizer.",
        "severity": "Medium"
    },
    "Tomato___Target_Spot": {
        "description": "Fungal disease caused by Corynespora cassiicola producing brown spots with light centers and dark concentric circles.",
        "treatment": "Apply fungicides containing Chlorothalonil or Azoxystrobin.",
        "prevention": "Improve plant spacing and remove crop debris after harvest.",
        "pesticide": "Chlorothalonil, Azoxystrobin",
        "organic": "Copper Fungicide",
        "watering": "Drip irrigation at root level.",
        "fertilizer": "Balanced tomato food.",
        "severity": "Medium"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "Viral infection transmitted by whiteflies, causing severe leaf curling, stunting, and complete yield loss.",
        "treatment": "No cure for infected plants. Remove infected plants to stop virus spread.",
        "prevention": "Control whiteflies using yellow sticky traps or insect nets; plant TYLCV-resistant varieties.",
        "pesticide": "Imidacloprid (for whitefly vector control)",
        "organic": "Neem Oil, Insecticidal Soap, or Pyrethrin for whiteflies",
        "watering": "Water normally.",
        "fertilizer": "Balanced fertilizer to support growth.",
        "severity": "Critical"
    },
    "Tomato___Tomato_mosaic_virus": {
        "description": "Viral disease causing mottled light/dark green mosaic patterns, leaf distortion, and stunted plant growth.",
        "treatment": "No chemical cure. Remove and destroy infected tomato plants.",
        "prevention": "Disinfect garden tools with 10% bleach, wash hands before handling plants, and buy certified virus-free seeds.",
        "pesticide": "None available",
        "organic": "None available",
        "watering": "Water soil without touching leaves.",
        "fertilizer": "Balanced plant nutrient mix.",
        "severity": "Critical"
    },
    "Tomato___healthy": {
        "description": "Tomato foliage is healthy, dark green, and free from leaf spots or viruses.",
        "treatment": "None required.",
        "prevention": "Prune sucker branches and stake stems for good vertical growth.",
        "pesticide": "None needed",
        "organic": "None needed",
        "watering": "Water deeply 2-3 times a week at root level.",
        "fertilizer": "Balanced tomato fertilizer with calcium to prevent blossom end rot.",
        "severity": "None"
    }
}