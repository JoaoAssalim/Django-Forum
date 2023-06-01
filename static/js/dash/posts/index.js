var openModalBtn = document.getElementById('open-modal-btn');
var modal = document.getElementById('modal');
var closeModalBtn = document.getElementsByClassName('close')[0];
var toggleButtons = document.getElementsByClassName("toggleButton");

openModalBtn.addEventListener('click', function() {
  modal.style.display = 'block';
});

closeModalBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

window.addEventListener('click', function(event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
});

function openModal(postId) {
  var modal = document.querySelector("#modal-" + postId);
  modal.style.display = "block";
}
function closeModal(postId) {
  var modal = document.querySelector("#modal-" + postId);
  modal.style.display = "none";
}


for (var i = 0; i < toggleButtons.length; i++) {
  toggleButtons[i].addEventListener("click", function() {
      var targetId = this.getAttribute("data-target");
      var contentDiv = document.querySelector(targetId);
      
      if (contentDiv.style.display === "none") {
          contentDiv.style.display = "block";
      } else {
          contentDiv.style.display = "none";
      }
  });
}


setTimeout(function() {
  var messages = document.getElementsByClassName('message')[0];
  if (messages) {
      messages.style.display = 'none';
  }
}, 5000);

function reloadTimer(){
  setTimeout(reload, 100)
}

function reload() {
  var posicao = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
  window.location.reload();

  setTimeout(function() {
      window.scrollTo(0, posicao);
  }, 0);
}