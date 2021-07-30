
const addNewCategoryBtn = document.getElementById("add-new-category-btn")
const bgModal = document.getElementById("bg-modal")
console.log("1")
addNewCategoryBtn.addEventListener("click", function () {
    bgModal.style.display = "block"
    console.log("2")
})

function closeModal() {
    bgModal.style.display = "none"
    console.log("hi from close modal")
}