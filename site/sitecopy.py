"""Namaste Beads (namastebeads.com): the flagship for beaded crystal jewelry, malas and bead strands. All copy is written for this site only."""
import re, collections
from copybase import E, stone_color, intent_color, kinds_phrase, kind_one, plist, tradition, hood_list, HOODS as HOOD_DATA

BEADY = re.compile(r'\bbead(s|ed)?\b|\d+ ?mm\b|chips?\b|\bmala\b|rudraksh|choker', re.I)
AISLES = {
 'beaded':   ('Beaded Bracelets', 'Bracelets', 'beaded-bracelets', 'Natural stone stretch bracelets, single-stone and mixed, from tiny 2 mm strands to bold 12 mm beads.', '#d9824b'),
 'mala':     ('Malas', 'Malas', 'malas', '108-bead necklace malas with guru bead and tassel, plus 27- and 54-bead wrist malas.', '#2f6f5e'),
 'necklace': ('Beaded Necklaces & Chokers', 'Necklaces', 'beaded-necklaces', 'Chip-stone chokers, bead necklaces and strung pendants.', '#8e5bb5'),
 'other':    ('Bead Rings, Anklets & Strands', 'Rings & Anklets', 'bead-rings-anklets', 'Beaded rings and anklets, waist beads and loose stone strands for stringing.', '#b8862b'),
}
def assign(x):
    b = x['base']
    if b == 'beaded': return 'beaded'
    if b == 'mala': return 'mala'
    if b == 'beads': return 'other'
    if b in ('necklace', 'pendant') and BEADY.search(x['title']): return 'necklace'
    if b in ('anklet', 'ring', 'earrings', 'bracelet') and BEADY.search(x['title']) and not re.search(r'band|domed|cuff|chain', x['title'], re.I): return 'other' if b != 'bracelet' else 'beaded'
    return None
LABELS = {'stone': 'Stone', 'metal': 'Strung on'}
PRICE_BANDS = [('0-10', 'Under $10'), ('0-15', 'Under $15'), ('15-25', '$15 to $25'), ('25-50', '$25 to $50'), ('50-99999', '$50 and up')]
BRAND_BANDS = [('Under $15', 0, 15), ('$15 to $30', 15, 30), ('$30 and up', 30, 1e9)]
STONE_MIN = 5; INTENT_MIN = 5; NAV_INTENTS = True

VISIT_EYEBROW = 'Come feel the beads'
def STORE_DESC(S): return f'Bead jewelry shop by Union Square in Manhattan: about {S.ABOUT_N:,} beaded crystal bracelets, malas, bead necklaces and strands in natural stones.'
REVIEW_TITLE = 'Wearing our beads?'
REVIEW_TEXT = 'A Google review helps other New Yorkers find natural stone beads near Union Square.'
LOGO_SVG = '<svg viewBox="0 0 40 40"><g fill="#d9824b"><circle cx="20" cy="7" r="3.6"/><circle cx="30.4" cy="13" r="3.6"/><circle cx="30.4" cy="26" r="3.6"/><circle cx="20" cy="32" r="3.6"/><circle cx="9.6" cy="26" r="3.6"/><circle cx="9.6" cy="13" r="3.6"/></g><circle cx="20" cy="19.5" r="3" fill="currentColor"/></svg>'
WORDMARK = 'Namaste <b>Beads</b>'
BAR_TEXT = 'Natural stone beads at 2 West 14th Street'
SEARCH_PLACEHOLDER = 'Search beads: 8mm amethyst, lava, mala'
QUIZ = {
 'slug': 'bracelet-finder', 'nav': 'Bracelet finder', 'cta': 'Find my beads',
 'title': 'Beaded Bracelet Finder', 'desc': 'Pick a color mood, a bead size and a budget and see matching beaded bracelets in stock at 2 West 14th Street.',
 'h1': 'Find your beads', 'lead': 'Three questions, then real bracelets from the bead wall. Runs in your browser; nothing is saved.', 'submit': 'Show my beads',
 'questions': [
  {'q': 'Which feeling are you after?', 'options': [{'label': 'Calm', 'filter': {'intent': ['calm']}}, {'label': 'Grounded', 'filter': {'intent': ['grounding']}},
    {'label': 'Protected', 'filter': {'intent': ['protection']}}, {'label': 'Lucky', 'filter': {'intent': ['abundance']}}, {'label': 'Loved', 'filter': {'intent': ['love']}}]},
  {'q': 'Bead size?', 'options': [{'label': 'Delicate, 2 to 6 mm', 'filter': {'mmax': 6}}, {'label': 'Classic 8 mm', 'filter': {'mmin': 7, 'mmax': 9}}, {'label': 'Bold, 10 mm and up', 'filter': {'mmin': 10}}, {'label': 'Any', 'filter': {}}]},
  {'q': 'Budget?', 'options': [{'label': 'Under $15', 'filter': {'maxp': 15}}, {'label': 'Under $25', 'filter': {'maxp': 25}}, {'label': 'Any', 'filter': {}}]},
 ]}
def FOOTER_EXPLORE(S):
    return [('Bead size guide', '/guide/bead-size-guide/'), ('Measure your wrist', '/guide/measure-your-wrist/'), ('Stretch bracelet care', '/guide/stretch-bracelet-care/'),
            ('Beads by stone', '/stones/'), ('Beads by intention', '/intentions/'), ('Bracelet finder', '/bracelet-finder/'), ('Bead shop in Manhattan', '/bead-jewelry-manhattan/')]
FOOT_BLURB = 'Beads in natural stone, wood and seed: bracelets, malas and strands, on 14th Street by Union Square.'
HERO_BASES = ('beaded', 'mala')
def HERO(S):
    return {'eyebrow': 'Natural stone beads &middot; 2 West 14th Street &middot; Manhattan',
            'h1': 'Beads you can feel, <em>in every stone.</em>',
            'lede': f'{S.N:,} beaded bracelets, malas, bead necklaces and strands in {len([k for k in S.stone_any if k not in S.NON_STONE])} kinds of stone, plus wood and rudraksha. From {S.money(S.MIN_PRICE)}. On 14th Street, minutes from Union Square.' + (f' Reserve online; ready {S.READY.lower().replace("usually ready ", "")}.' if S.PICKUP_ON else ''),
            'shop_cta': 'Shop beads'}
def _sizes(S):
    rows = [('2-4', 'Mini', 0, 4.5), ('6', 'Petite', 4.6, 6.9), ('8', 'Classic', 7, 9), ('10-12', 'Bold', 9.1, 20)]
    tiles = ''.join(f'<a class="scent" href="/bead-size/{k}mm/" style="--c:#d9824b"><b>{k} mm</b><span>{lab}</span><small>{sum(1 for x in S.products if x["mm"] and lo <= x["mm"] <= hi)} pieces</small></a>' for k, lab, lo, hi in rows)
    return f'<section class="wrap"><div class="sechead"><h2>Shop by bead size</h2><a href="/guide/bead-size-guide/">Size guide &rarr;</a></div><div class="scents">{tiles}</div></section>'
def _stones(S):
    keys = [k for k in S.STONE_KEYS][:18]
    chips = ''.join(f'<a class="chip" href="/stones/{k}/">{E(S.STONE_NAME[k])} <small>{S.stone_any[k]}</small></a>' for k in keys)
    return f'<section class="wrap"><div class="sechead"><h2>Beads by stone</h2><a href="/stones/">All stones &rarr;</a></div><div class="chips">{chips}</div></section>'
def _near(S): return f'<section class="wrap"><div class="sechead"><h2>Find the bead wall from</h2></div>{hood_list(S, "/near/")}</section>'
def _whys(S):
    return [(f'{S.N:,} bead pieces', 'Bracelets, malas, chokers and strands, each with its own photo and price.'),
            ('Every bead size', 'From 2 mm micro strands to 12 mm statement beads, labeled in the title.'),
            (('Reserve and pick up', f'Choose Pickup at checkout. Orders are {S.READY.lower()}.') if S.PICKUP_ON else ('', '')),
            ('Stone, wood and seed', 'Natural stones alongside sandalwood, rudraksha and lava.'),
            ('Big-wrist sizes', 'Look for BIG Wrist in the title for 8 to 8.5 inch bracelets.'),
            ('Open daily', 'From 11 AM, until 9 PM on Fridays and Saturdays.')]
def _best(S): return S.by_rank(S.leaders)[:8]
def _malas(S): return S.by_rank([x for x in S.leaders if x['aisle'] == 'mala' and not x['noimg']])[:4]
def _mixed(S): return S.by_rank([x for x in S.leaders if len(x['stones']) > 1 and x['aisle'] == 'beaded' and not x['noimg']])[:8]
HOME_SECTIONS = [
 {'type': 'html', 'html': _sizes},
 {'type': 'grid', 'title': 'Best-selling beads', 'select': _best, 'href': '/shop/', 'link': 'All beads', 'intro': 'In order of sales on namastebookshop.com, refreshed each day.'},
 {'type': 'html', 'html': _stones},
 {'type': 'visit'},
 {'type': 'grid', 'title': 'Malas', 'select': _malas, 'href': '/shop/malas/', 'link': 'All malas'},
 {'type': 'collections', 'title': 'Bead collections', 'items': [
   {'title': 'Chakra beads', 'blurb': 'Seven-stone strands.', 'href': '/intentions/chakra/', 'filter': {'intent': ['chakra']}},
   {'title': 'Lava & diffuser beads', 'blurb': 'Porous lava for a drop of oil.', 'href': '/lava-bead-bracelets/', 'filter': {'q': 'lava'}},
   {'title': 'Chip bracelets', 'blurb': 'Tumbled stone chips.', 'href': '/chip-bead-bracelets/', 'filter': {'q': 'chip'}},
   {'title': 'Wood & seed beads', 'blurb': 'Sandalwood, rudraksha, tulsi.', 'href': '/stones/wood/', 'filter': {'stone': ['wood', 'rudraksha', 'sandalwood']}},
   {'title': 'Big wrist', 'blurb': '8 to 8.5 inch fits.', 'href': '/big-wrist-beaded-bracelets/', 'filter': {'q': 'big wrist|large wrist|xl'}},
   {'title': 'Chokers', 'blurb': 'Chip stones on a clasp.', 'href': '/shop/beaded-necklaces/', 'filter': {'aisle': ['necklace']}}]},
 {'type': 'grid', 'title': 'Two stones or more', 'select': _mixed, 'href': '/shop/beaded-bracelets/', 'link': 'All bracelets'},
 {'type': 'whys', 'title': 'Why the bead wall', 'items': _whys},
 {'type': 'quiz', 'title': 'Not sure which beads?', 'text': 'Pick a feeling, a bead size and a budget.'},
 {'type': 'brands', 'title': 'Bead makers', 'n': 10},
 {'type': 'html', 'html': _near},
 {'type': 'review'},
 {'type': 'band', 'title': 'Reserve beads, pick them up', 'text': lambda S: 'Every strand online is a live listing. Reserve and collect on 14th Street, or ship from New York City.',
  'steps': lambda S: [('Choose stone and size', 'Filter by stone, size, price and style.'), ('Pickup at checkout', f'Secure Shopify checkout. {S.READY or "Usually ready the same day"}.'), ('Collect', S.STORE_ADDR + '.')]},
]
def HOME_TITLE(S): return 'Namaste Beads | Beaded Crystal Bracelets & Malas near Union Square, NYC'
def HOME_DESC(S): return f'{S.N:,} natural stone beaded bracelets, malas, bead necklaces and strands at {S.STORE_ADDR}, by Union Square. Every bead size, from {S.money(S.MIN_PRICE)}. Pickup or ship.'
def SHOP_TITLE(S): return 'Shop Beaded Crystal Jewelry Online | Namaste Beads NYC'
def SHOP_DESC(S): return f'{S.N:,} beaded bracelets, malas and bead necklaces in natural stone from {S.money(S.MIN_PRICE)}. Pick up at 2 West 14th Street or ship.'
SHOP_H1 = 'All beads'
def SHOP_SUB(S): return f'{S.N:,} pieces. Filter by stone, style, brand and price.'
def AISLE_TITLE(S, k): return f'{AISLES[k][0]} in NYC | Namaste Beads, Union Square'
def AISLE_DESC(S, k): return f'{AISLES[k][3]} {S.cat_count[k]} in stock at 2 West 14th Street.'
def LANDINGS(S):
    L = [{'path': '/lava-bead-bracelets/', 'title': 'Lava Bead Bracelets in NYC | Namaste Beads', 'desc': 'Lava stone bead bracelets near Union Square. Porous lava beads hold a drop of essential oil.', 'h1': 'Lava bead bracelets', 'sub': 'Porous volcanic beads that hold a drop of oil.', 'filter': {'q': 'lava'}},
         {'path': '/chip-bead-bracelets/', 'title': 'Crystal Chip Bracelets | Namaste Beads NYC', 'desc': 'Tumbled crystal chip bracelets and chokers at 2 West 14th Street.', 'h1': 'Chip bead jewelry', 'sub': 'Small tumbled stone chips, strung close.', 'filter': {'q': 'chip'}},
         {'path': '/big-wrist-beaded-bracelets/', 'title': 'Big Wrist Beaded Bracelets 8 to 8.5 Inch | Namaste Beads', 'desc': 'Larger-fit beaded crystal bracelets for bigger wrists, at 2 West 14th Street.', 'h1': 'Big-wrist bracelets', 'sub': 'Strung longer for 8 to 8.5 inch wrists.', 'filter': {'q': 'big wrist|large wrist|xl'}}]
    for k, lab, lo, hi in (('2-4', 'Mini', 0, 4.5), ('6', 'Petite', 4.6, 6.9), ('8', 'Classic', 7, 9), ('10-12', 'Bold', 9.1, 20)):
        L.append({'path': f'/bead-size/{k}mm/', 'title': f'{k}mm Beaded Bracelets & Malas | Namaste Beads NYC', 'desc': f'{lab} {k} mm natural stone beaded bracelets and malas at 2 West 14th Street near Union Square.',
                  'h1': f'{k} mm beads', 'sub': f'{lab} beads, measured across the bead.', 'filter': {'mmin': lo, 'mmax': hi}})
    return L
def stone_tile(S, k):
    tr = tradition(S, k); return f'Bead lore: {plist(tr[:2])}.' if tr else 'Natural beads.'
def STONE_PAGE(S, k, xs):
    n = S.STONE_NAME[k]; tr = tradition(S, k); mm = sorted({x['mm'] for x in xs if x['mm']})
    intro = (f'<p class="intro">{len(xs)} {E(n.lower())} bead pieces: {kinds_phrase(S.kinds_of(xs))}.' + (f' Bead sizes from {mm[0]:g} to {mm[-1]:g} mm.' if mm else '') + '</p>'
             + (f'<p class="note-belief">Bead traditions associate {E(n.lower())} with {plist(tr)}. That is lore people enjoy, not a proven effect.</p>' if tr else ''))
    return {'title': f'{n} Beads: Bracelets & Malas in NYC | Namaste Beads', 'desc': f'{len(xs)} {n.lower()} beaded bracelets, malas and bead necklaces from {S.money(min(x["price"] for x in xs))} at 2 West 14th Street.',
            'h1': f'{n} beads', 'sub': f'{len(xs)} pieces', 'intro': intro,
            'faq': [(f'What bead sizes do you have in {n.lower()}?', (f'Right now {", ".join(f"{m:g}" for m in mm)} mm.' if mm else 'Sizes are in each title.')), (f'Where can I buy {n.lower()} beads in Manhattan?', f'At {S.STORE_ADDR}, by Union Square.')], 'faq_title': f'{n} bead questions'}
def intent_tile(S, k): return f'{S.intent_count[k]} bead pieces'
def INTENT_PAGE(S, k, xs):
    n = S.INTENT_NAME[k]; st = [S.STONE_NAME[s] for ik, _, sts, _ in S.INTENTS if ik == k for s in sts if s in S.STONE_NAME]
    return {'title': f'{n} Beads & Bracelets | Namaste Beads NYC', 'desc': f'{len(xs)} beaded bracelets and malas chosen for {n.lower()}, at 2 West 14th Street near Union Square.',
            'h1': f'Beads for {n.lower()}', 'sub': f'{len(xs)} pieces', 'intro': f'<p class="intro">Stones bead-wearers reach for when they set this intention' + (f': {E(plist(st[:4]).lower())}' if st else '') + '.</p><p class="note-belief">Tradition and personal meaning only; we make no claims about effects.</p>',
            'faq': [(f'Which beads are worn for {n.lower()}?', (f'Most often {plist(st[:5]).lower()}, according to crystal tradition.' if st else 'See the pieces above.'))]}
def STONES_HUB(S): return {'title': 'Beads by Stone | Namaste Beads NYC', 'desc': 'Natural stone beads by stone, with sizes and counts.', 'h1': 'Beads by stone', 'lead': 'Every stone we have strung on bracelets, malas or necklaces.'}
def INTENTS_HUB(S): return {'title': 'Beads by Intention | Namaste Beads NYC', 'desc': 'Beaded bracelets and malas grouped by the intention tradition gives each stone.', 'h1': 'Beads by intention', 'lead': 'Grouped by bead lore, shared as tradition only.'}
def brand_intro(S, k, st):
    xs = st['xs']; mm = sorted({x['mm'] for x in xs if x['mm']})
    return f'<p>{st["n"]} {E(S.BRAND_NAME[k])} bead piece{"s" if st["n"] != 1 else ""}: {kinds_phrase(S.kinds_of(xs))}' + (f', beads from {mm[0]:g} to {mm[-1]:g} mm' if len(mm) > 1 else '') + f'. From {S.money(st["min"])}.</p>'
def brand_faq(S, k, st): return [(f'Where can I find {S.BRAND_NAME[k]} beads in NYC?', f'At Namaste Beads, {S.STORE_ADDR}, with {st["n"]} pieces today.')]
def BRAND_H1(S, k): return f'{S.BRAND_NAME[k]} beads'
def BRAND_TITLE(S, k, st): return f'{S.BRAND_NAME[k]} Beaded Bracelets | Namaste Beads NYC'
def BRAND_DESC(S, k, st): return f'{st["n"]} {S.BRAND_NAME[k]} beaded pieces from {S.money(st["min"])} at 2 West 14th Street.'
def BRANDS_TITLE(S): return 'Bead Brands & Makers | Namaste Beads NYC'
def BRANDS_DESC(S): return 'Named bead jewelry brands at Namaste Beads, 2 West 14th Street.'
BRANDS_H1 = 'Bead makers'
def BRANDS_LEAD(S, n): return f'{n} named makers. Most of our beads come from independent stringers and are easiest to find <a href="/stones/">by stone</a>.'
PAIR = {'beaded': ['beaded'], 'mala': ['beaded'], 'necklace': ['beaded'], 'beads': ['mala'], 'anklet': ['beaded'], 'ring': ['beaded'], 'earrings': ['necklace'], 'bracelet': ['beaded'], 'pendant': ['beaded']}
REL_BRAND = 'More by {brand}'
REL_SCENT = 'More {scent} beads'
REL_PAIR = 'Stack it with'
REL_MORE = 'More {aisle}'
def describe(S, x):
    k = x['base']; stn = x['stones']; s = []
    s.append(f"{E(x['title'])}: " + (f"{E(plist([S.STONE_NAME[t] for t in stn[:3]]).lower())} " if stn else '') + ('beads' if k != 'mala' else 'mala beads') + (f" at about {x['mm']:g} mm each" if x['mm'] else '') + '.')
    if k == 'beaded': s.append('Strung on stretch cord to slip over the hand. Standard fits suit most wrists around 6.5 to 7 inches; BIG Wrist titles run longer.')
    if k == 'mala': s.append('A mala is a strand of prayer beads used to count repetitions in meditation; 108 beads is the traditional full count.')
    if stn and stn[0] not in S.NON_STONE and tradition(S, stn[0]): s.append(f"Bead lore pairs {E(S.STONE_NAME[stn[0]].lower())} with {plist(tradition(S, stn[0]))}; enjoy it as tradition, not as a claim.")
    s.append('Natural stones vary from bead to bead, so color and pattern will differ slightly from the photo.')
    s.append('Keep stretch cord away from water and lotion and roll it on and off. Pick up at 2 West 14th Street or ship from NYC; checkout is on Shopify through namastebookshop.com.')
    return s
def PRODUCT_DESC(S, x, v0): return f"{x['title']}, {S.money(v0['price'])}. Natural beads at 2 West 14th Street by Union Square" + (', pickup in about 2 hours.' if x['pickup'] else '.')
def ABOUT_DESC(S): return 'About Namaste Beads, the bead jewelry shop at 2 West 14th Street by Union Square. A brand of Wealth Edge Ventures Inc.'
ABOUT_H1 = 'About Namaste Beads'
def ABOUT(S):
    return f'''<p class="lead">Namaste Beads is the bead wall at {S.STORE_ADDR}: stretch bracelets, malas, chip chokers and strands in natural stone, wood and seed.</p>
<p>{S.N:,} pieces are listed online with bead sizes in the titles, so you can match a stack before you come in.{" Reserve and choose Pickup at checkout." if S.PICKUP_ON else ""}</p>
<h2>Visit</h2><p>{S.STORE_ADDR}. Call <a href="tel:{S.TEL}">{S.PHONE}</a>.</p>{S.hours_html()}{S.visit_buttons()}
<h2>Who we are</h2><p>{S.LEGAL} Payment, shipping and pickups run through our Shopify store, <a href="{S.SHOP}" rel="noopener">namastebookshop.com</a>.</p>
<h2>Bead lore</h2><p>We share what traditions say about stones, clearly as tradition. Nothing here is medical advice.</p>'''
VISIT_TITLE = 'Visit the Bead Wall near Union Square'
def VISIT_DESC(S): return f'Hours, subway directions and pickup for Namaste Beads at {S.STORE_ADDR}, by Union Square.'
def VISIT_LEAD(S): return f'The bead wall is at {S.STORE_ADDR}, a few minutes west of Union Square on 14th Street.'
def FAQ_DESC(S): return 'Bead questions: sizes, wrist fit, stretch cord care, malas, pickup and shipping at Namaste Beads.'
FAQ_H1 = 'Bead questions'
def FAQ(S):
    return [('What size bead should I choose?', 'Most people start with 8 mm. Smaller beads look delicate and stack well; 10 to 12 mm is bold. See the <a href="/guide/bead-size-guide/">bead size guide</a>.'),
            ('Will a bracelet fit my wrist?', 'Standard stretch bracelets fit most wrists around 6.5 to 7 inches. Measure with the <a href="/guide/measure-your-wrist/">wrist guide</a>, and look for BIG Wrist titles for larger fits.'),
            ('What is a mala?', 'A strand of prayer beads, traditionally 108, used to count mantras or breaths. Our sister shop <a href="https://namastebeadshop.com/">Namaste Bead Shop</a> goes deeper.'),
            ('How do I keep stretch cord from breaking?', 'Roll the bracelet on and off and keep it dry. See <a href="/guide/stretch-bracelet-care/">bracelet care</a>.'),
            ('Can I reserve beads and pick them up?', 'Yes, choose Pickup at checkout.' + (f' Orders are {S.READY.lower()}.' if S.READY else '')),
            ('Where are you?', f'{S.STORE_ADDR}, about a 4-minute walk from 14 St&ndash;Union Square.'),
            ('Do beads have healing powers?', 'Traditions give stones meanings, and we share them as lore. We do not claim any health effect.')]
def GUIDES(S):
    return [
     {'path': '/guide/bead-size-guide/', 'title': 'Bead Size Guide: 4mm vs 6mm vs 8mm vs 10mm Bracelets', 'desc': 'How bead sizes look on the wrist, from 2 mm micro beads to 12 mm statement beads, and how to mix sizes in a stack.', 'h1': 'Bead size guide',
      'html': '''<p class="lead">Bead size is the diameter of a single bead in millimeters, and it changes the whole look of a bracelet.</p><ul><li><b>2 to 4 mm:</b> fine and delicate; great for stacking several.</li><li><b>6 mm:</b> petite, everyday and office-friendly.</li><li><b>8 mm:</b> the classic size, and the most common on our wall.</li><li><b>10 to 12 mm:</b> bold and chunky; reads as a statement piece.</li></ul><h2>Stacking</h2><p>Mix one bold strand with two finer ones, or keep one size and vary the stones.</p><p><a class="btn" href="/bead-size/8mm/">Shop 8 mm</a></p>'''},
     {'path': '/guide/measure-your-wrist/', 'title': 'How to Measure Your Wrist for a Beaded Bracelet', 'desc': 'Measure your wrist with string or a tape and choose a beaded bracelet that fits.', 'h1': 'Measure your wrist',
      'html': '''<p class="lead">Wrap a soft tape or a strip of paper snugly around your wrist just below the wrist bone, then add about half an inch for a comfortable stretch fit.</p><ul><li>Under 6.5 inches: standard bracelets will feel a little loose.</li><li>6.5 to 7 inches: standard fit.</li><li>7.5 inches and up: look for BIG Wrist or 8 to 8.5 inch titles.</li></ul><p>Bigger beads take up more room inside the circle, so they fit slightly snugger at the same length.</p>'''},
     {'path': '/guide/stretch-bracelet-care/', 'title': 'Stretch Bracelet Care: Make Beaded Bracelets Last', 'desc': 'Simple ways to keep beaded stretch bracelets from breaking.', 'h1': 'Stretch bracelet care',
      'html': '''<p class="lead">Elastic cord is the part that wears out, not the stone.</p><ul><li>Roll bracelets on and off over your hand; do not pull them wide.</li><li>Take them off for showers, swimming and dishes.</li><li>Keep lotion and sanitizer off the cord.</li><li>Store them flat, not stretched over a bottle or stand.</li><li>Porous stones such as lava, turquoise and malachite prefer to stay dry.</li></ul>'''},
     {'path': '/bead-jewelry-manhattan/', 'title': 'Bead Jewelry Shop in Manhattan near Union Square', 'store_ld': True, 'desc': f'Beaded bracelets and malas in Manhattan: {S.N:,} natural stone bead pieces at {S.STORE_ADDR}.', 'h1': 'A bead shop in Manhattan',
      'html': f'<p class="lead">{S.N:,} bead pieces in natural stone, wood and seed, on 14th Street just west of Fifth Avenue.</p>{hood_list(S, "/near/")}{S.visit_block()}'},
    ]
HOOD_LINE = {'union-square': 'Beads a few minutes from the Union Square Greenmarket.', 'east-village': 'From the East Village, stay on 14th Street heading west.', 'chelsea': 'From Chelsea, cross Sixth Avenue on 14th.',
             'flatiron': 'From Flatiron, a ten-block walk down Fifth.', 'greenwich-village': 'From Washington Square, head north on Fifth.', 'midtown': 'From Midtown, ride down to Union Square.'}
def HOODS(S):
    picks = S.by_rank([x for x in S.leaders if not x['noimg']])[:8]
    return [{'path': f'/near/{k}/', 'title': f'Beaded Bracelets & Malas near {n} | Namaste Beads', 'h1': f'Beads near {n}', 'desc': f'Natural stone beaded bracelets and malas near {n}, NYC: {S.N:,} pieces at {S.STORE_ADDR}.',
             'html': f'<p class="lead">{E(HOOD_LINE[k])} {S.N:,} bead pieces waiting.</p><h2>From {E(n)}</h2><p>{E(route)}</p><h2>On the bead wall</h2>{S.grid(picks)}{S.visit_block()}<h2>Other neighborhoods</h2>{hood_list(S, "/near/", k)}'}
            for k, n, route in HOOD_DATA]
NOT_FOUND = 'Those beads have rolled away'
