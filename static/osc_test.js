document.addEventListener("DOMContentLoaded", function(){
    setInterval(() => {
        fetch_data()
    }, 5000);
})

function fetch_data(){
    fetch("/get_initial_showfile_data")
    .then(response => response.json())
    .then(data => {
        document.getElementById("patch_count").innerHTML = data["patch_count"]
        document.getElementById("preset_count").innerHTML = data["preset_count"]
        document.getElementById("cp_count").innerHTML = data["cp_count"]
        document.getElementById("group_count").innerHTML = data["group_count"]
    })
    fetch("/get_channels_in_use")
    .then(response => response.json())
    .then(data => {
        const ulElement = document.getElementById("channels_in_use")
        if(ulElement === data){
            pass
        }else{
            data.forEach(item => {
                const liElement = document.createElement("li")
                liElement.textContent = item
                ulElement.appendChild(liElement)
            });
        }
    });
}