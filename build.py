from staticjinja import Site

about = {
    "about_greeting": "Hello World 🌍",
    "about_description": "I'm Divin, a data scientist with a passion for uncovering insights through data exploration. I also enjoy creating games, music, and art in my free time and showcase my work on GitHub, YouTube, itch.io, Bandcamp and SoundCloud. When I'm not working, I'm a proud dog dad. Check out my links below to see my latest work! 👇",
}

event_1 = {
    "icon": "fas fa-briefcase",
    "timeframe": "2023 - today",
    "company": "Smart Digital GmbH",
    "job": "Data Scientist",
    "description": "As an experienced Python developer with a solid background in statistical analysis, my focus is on extracting actionable insights from complex datasets. Leveraging my applied knowledge, I specialize in building sophisticated machine learning models, and proactively extend existing codebases to automate the analysis process even further.",
}

event_2 = {
    "icon": "fas fa-graduation-cap",
    "timeframe": "2022 - 2023",
    "company": "University Tübingen",
    "job": "Physics, M. Sc.",
    "description": "For my Master's thesis, I developed expertise in automating experimental data analysis using deep learning techniques. I focused on improving the performance of an existing object recognition model based on Faster R-CNN by using hyperparameter optimization to achieve better detection results of diffraction patterns in experimental data. Additionally, I designed and created a smaller YOLO-based model that was capable of performing similar tasks as the original model, but with significantly faster processing times.",
}

event_3 = {
    "icon": "fas fa-graduation-cap",
    "timeframe": "2016 - 2022",
    "company": "University Tübingen",
    "job": "Physics, B. Sc.",
    "description": "Through my studies in physics, I developed a solid foundation in both fundamental and advanced topics. As I continued to pursue my education, I focused on specializing in computational physics, taking computer science courses and developing strong proficiency in Python. For my Bachelor's thesis, I conducted research on the formation of planets on a protoplanetary disk, gaining valuable insights into the migration of planets driven by the disk torques and offering a unique perspective on these phenomena.",
}

cv = {
    "cv_description": "What I've achieved so far 🏆:",
    "cv_events": [event_1, event_2, event_3],
}

contact = {
    "contact_description": "Any questions? Would like to chat? Feel free to contact me 🤩",
}

github = {
    "url": "https://github.com/divin",
    "icon": "fab fa-github",
}

youtube = {
    "url": "https://www.youtube.com/@divingavran",
    "icon": "fab fa-youtube",
}

itchio = {
    "url": "https://divingavran.itch.io",
    "icon": "fab fa-itch-io",
}

bandcamp = {
    "url": "https://divin.bandcamp.com",
    "icon": "fab fa-bandcamp",
}

soundcloud = {
    "url": "https://soundcloud.com/divingavran",
    "icon": "fab fa-soundcloud",
}

social = {"social_links": [github, youtube, itchio, bandcamp, soundcloud]}

context = {}
context.update(cv)
context.update(about)
context.update(social)
context.update(contact)

if __name__ == "__main__":
    site = Site.make_site(
        searchpath="./templates",
        outpath="./build/",
        contexts=[("index.html", context)],
        staticpaths=["./static"],
    )

    site.render()
