$(document).ready(function() {
    let inventory = [];
  
    function displayInventory() {
      $("#inventory-list").empty();
      inventory.forEach(function(item, index) {
        $("#inventory-list").append(`<div>${item.name} - ${item.quantity} <button class="delete-item" data-index="${index}">Delete</button></div>`);
      });
    }
  
    function addItem(name, quantity) {
      inventory.push({ name: name, quantity: quantity });
      displayInventory();
    }
  
    function deleteItem(index) {
      inventory.splice(index, 1);
      displayInventory();
    }
  
    $.getJSON("inventory.json", function(data) {
      inventory = data;
      displayInventory();
    });
  
    // Add new item to inventory
    $("#inventory-form").submit(function(event) {
      event.preventDefault();
      const itemName = $("#item-name").val();
      const itemQuantity = $("#item-quantity").val();
      addItem(itemName, itemQuantity);
      $("#item-name").val("");
      $("#item-quantity").val("");
    });
  
    $("#display-inventory").click(function() {
      let modalContent = "<h2>Entire Inventory</h2><ul>";
      inventory.forEach(function(item) {
        modalContent += `<li>${item.name} - ${item.quantity}</li>`;
      });
      modalContent += "</ul>";
      $("#inventory-details").html(modalContent);
      $("#inventory-modal").css("display", "block");
    });
  
    $(".close, #inventory-modal").click(function() {
      $("#inventory-modal").css("display", "none");
    });
  
    $(".modal-content").click(function(event) {
      event.stopPropagation();
    });
  
    $(document).on("click", ".delete-item", function() {
      const index = $(this).data("index");
      deleteItem(index);
    });
  });
  