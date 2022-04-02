async function onClick(event){
    event.preventDefault();

    const selectLink = event.target;
    response = await fetch(selectLink.href);

    let responseData = await response.json()

    if (response.ok) {
        const photoId = selectLink.dataset.photoId;
        let selectCounter = document.getElementById(`select-counter-${photoId}`);
        selectCounter.innerText = `Selected: ${responseData.select_count}`;

         for (selectLinkToToggle of document.querySelectorAll(`a[data-photo-id="${photoId}"]`)) {
            selectLinkToToggle.classList.toggle("invisible");
        }

    } else {
        alert(responseData.error);
    }
}

function onLoad(){
    for (element of document.getElementsByClassName("select-link")) {
        element.addEventListener("click", onClick);
    }
}

window.addEventListener("load", onLoad);