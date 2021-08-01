
const bgModal1 = document.getElementById("bg-modal1")
const addNewCategoryBtn = document.getElementById("add-new-category-btn")
const bgModal = document.getElementById("bg-modal")
const numberOfSizesInput = document.getElementById("number-of-sizes")
let numberOfSizes = 1

function addProduct() {
    bgModal1.style.display = "block"
}

addNewCategoryBtn.addEventListener("click", function () {
    bgModal.style.display = "block"
})

function closeModal1() {
    bgModal1.style.display = "none"
    numberOfSizes = 0
}

function closeModal() {
    bgModal.style.display = "none"
}

function createNewInput(addAnotherSizeBtn) {
    numberOfSizes ++
    numberOfSizesInput.value = numberOfSizes
    let newContent = `<br><input type="text" id="product-sizes${numberOfSizes}" name="product-sizes${numberOfSizes}" required placeholder="Enter a size">`
    let container = addAnotherSizeBtn.parentNode.firstElementChild
    container.innerHTML += newContent
}