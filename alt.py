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
