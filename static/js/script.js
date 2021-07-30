
// const addNewProductBtn = document.getElementById("add-product")
const bgModal1 = document.getElementById("bg-modal1")
const addNewCategoryBtn = document.getElementById("add-new-category-btn")
const bgModal = document.getElementById("bg-modal")

// addNewProductBtn.addEventListener("click", function () {
//     bgModal1.style.display = "block"
//     console.log("here")
// })
console.log("hhhhi")
function addProduct() {
    bgModal1.style.display = "block"
    console.log("here")
}

addNewCategoryBtn.addEventListener("click", function () {
    bgModal.style.display = "block"
})

function closeModal1() {
    bgModal1.style.display = "none"
}

function closeModal() {
    bgModal.style.display = "none"
}