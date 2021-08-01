
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

function closeModal1(item) {
    bgModal1.style.display = "none"
    numberOfSizes = 0
    location.reload();
    // $(item).find('form')[0].trigger('reset');

}

// $('.modal_').on('hidden', function(){
//     $(this).find('form')[0].reset();
// });

function closeModal() {
    bgModal.style.display = "none"
    location.reload();
}

function createNewInput(addAnotherSizeBtn) {
    numberOfSizes ++
    numberOfSizesInput.value = numberOfSizes
    let newContent = `<br><input type="text" id="product-sizes${numberOfSizes}" name="product-sizes${numberOfSizes}" required placeholder="Enter a size">`
    let container = addAnotherSizeBtn.parentNode.firstElementChild
    let tempInputs = []
    elements_ = container.getElementsByTagName("*")
    for (let i=2, j=0; i<=2*numberOfSizes-1; i+=2, j++){
        console.log(elements_[i])
        tempInputs.push(elements_[i].value)
        // console.log(tempInputs[j])
    }
    container.innerHTML += newContent
    for (let i=2, j=0; i<=2*numberOfSizes-1; i+=2, j++)
        elements_[i].value = tempInputs[j]
}