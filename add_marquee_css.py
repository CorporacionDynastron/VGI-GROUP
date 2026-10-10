import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

marquee_css = """
        @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            display: flex;
            width: max-content;
            animation: marquee 20s linear infinite;
        }
"""

if '@keyframes marquee' not in html:
    html = html.replace('</style>', marquee_css + '    </style>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added CSS for marquee")
else:
    print("CSS already there")
