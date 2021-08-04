
const bgModal1 = document.getElementById("bg-modal1")
const addNewCategoryBtn = document.getElementById("add-new-category-btn")
const bgModal = document.getElementById("bg-modal")
const numberOfSizesInput = document.getElementById("number-of-sizes")
let numberOfSizes = 1

let number_of_images
let images_url_list = []
let images_list
let currentImage
let imageNumberMessage
let currentImageNumber

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
    let newContent = `<br><input type="text" id="product-sizes${numberOfSizes}" name="product-sizes${numberOfSizes}" required placeholder="Enter a size" style="margin-bottom: 5px">`
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

function getData(item) {
    number_of_images = item.value
    images_url_list = []
    images_list = item.parentNode.parentNode.getElementsByTagName('input')
    currentImage = item.parentNode.parentNode.getElementsByTagName('img')
    imageNumberMessage = item.parentNode.parentNode.getElementsByTagName('span')[0]
    currentImageNumber = images_list[0].value
}

function nextImage(item){
    getData(item)
    for (let i=1; i<=number_of_images; i++){
        images_url_list.push(images_list[i].value)
    }
    if(number_of_images > 0){
        if(parseInt(currentImageNumber) === parseInt(number_of_images)) { // display the first image
            currentImage[0].src = images_url_list[0]
            images_list[0].value = 1
        }else {
                currentImage[0].src = images_url_list[parseInt(currentImageNumber)]
                images_list[0].value = parseInt(currentImageNumber) + 1
        }
    }
    imageNumberMessage.textContent = "Image " + (images_list[0].value).toString() + " of " + (number_of_images).toString()
}

function prevImage(item) {
    getData(item)
    for (let i=1; i<=number_of_images; i++){
        images_url_list.push(images_list[i].value)
    }
    if(number_of_images !== 0){
        if(parseInt(currentImageNumber) === 1) { // display the first image
            currentImage[0].src = images_url_list[parseInt(number_of_images) -1]
            images_list[0].value = parseInt(number_of_images)
        }else {
                currentImage[0].src = images_url_list[parseInt(currentImageNumber)-2]
                images_list[0].value = parseInt(currentImageNumber) - 1
        }
    }
    imageNumberMessage.textContent = "Image " + (images_list[0].value).toString() + " of " + (number_of_images).toString()
}