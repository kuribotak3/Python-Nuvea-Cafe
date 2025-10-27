document.addEventListener("DOMContentLoaded", function () {
  const cashInput = document.getElementById("cashInput");
  const paymentRadios = document.querySelectorAll(
    "input[name='paymentMethod']"
  );

  paymentRadios.forEach((radio) => {
    radio.addEventListener("change", () => {
      if (radio.value === "cash" && radio.checked) {
        cashInput.style.display = "block";
      } else if (radio.checked) {
        cashInput.style.display = "none";
      }
    });
  });

  // Tampilkan input jika default-nya Tunai
  const defaultChecked = document.querySelector(
    "input[name='paymentMethod']:checked"
  );
  if (defaultChecked && defaultChecked.value === "cash") {
    cashInput.style.display = "block";
  }
});
