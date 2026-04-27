from pyscript import document # type: ignore

Olmedo = [
    {
        "img": "https://i.pinimg.com/736x/4d/21/e1/4d21e1c2c27672c316f284d44a03ea83.jpg",
        "caption": "Description"
    },
    {
        "img": "https://i.pinimg.com/1200x/6b/6a/ab/6b6aab076c556b70d434d7b848806ef4.jpg",
        "caption": "Description"
    },
    {
        "img": "https://i.pinimg.com/736x/30/8f/66/308f66f49f56ba3957be226d6c25117c.jpg",
        "caption": "Description"
    }
]


Baring = [
    {
        "img": "https://i.pinimg.com/736x/5e/17/d0/5e17d09d26f477c08755907890032884.jpg",
        "caption": "Description"
    },
    {
        "img": "https://i.pinimg.com/736x/4d/21/e1/4d21e1c2c27672c316f284d44a03ea83.jpg",
        "caption": "Description"
    },
    {
        "img": "https://i.pinimg.com/1200x/6b/6a/ab/6b6aab076c556b70d434d7b848806ef4.jpg",
        "caption": "Description"
    }
]

def create_cards(data, container_id):
    container = document.getElementById(container_id)

    for item in data:
        card = document.createElement("div")
        card.className = "flip-card"

        card.innerHTML = f"""
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <img src="{item['img']}">
            </div>
            <div class="flip-card-back">
                <p>{item['caption']}</p>
            </div>
        </div>
        """

        container.appendChild(card)

create_cards(Olmedo, "Olmedo-gallery")
create_cards(Baring, "Baring-gallery")


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return (
            f"Hello! My name is {self.name}. "
            f"I am from 10 {self.section}, "
            f"and my favorite subject is {self.favorite_subject}."
        )


classmates = [
    Classmate("Lauren Villafuerte", "Ruby", "English"),
    Classmate("Jaiyanah Baring", "Ruby", "Mathematics"),
    Classmate("Amanda Yao", "Ruby", "Music & Arts"),
    Classmate("Aisha Ledesma", "Ruby", "Science"),
    Classmate("Shalanie Garabiles", "Ruby", "Music & Arts"),
]


def show_list(event=None):
    output = document.getElementById("output")

    introductions = []
    for number, classmate in enumerate(classmates, start=1):
        introductions.append(f"{number}. {classmate.introduce()}")

    output.innerHTML = "<br><br>".join(introductions)


def add_classmate(event=None):
    name_input = document.getElementById("name")
    section_input = document.getElementById("section")
    subject_input = document.getElementById("subject")
    output = document.getElementById("output")

    name = name_input.value.strip()
    section = section_input.value.strip()
    favorite_subject = subject_input.value.strip()

    if not name or not section or not favorite_subject:
        output.innerHTML = "Please complete the name, section, and favorite subject first."
        return

    new_classmate = Classmate(name, section, favorite_subject)
    classmates.append(new_classmate)

    output.innerHTML = (
        "New classmate added successfully!<br><br>"
        f"{new_classmate.introduce()}<br><br>"
        f"There are now {len(classmates)} classmates in the list."
    )

    name_input.value = ""
    section_input.value = ""
    subject_input.value = ""
