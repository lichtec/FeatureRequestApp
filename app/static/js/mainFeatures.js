function Feature(data) {
  this.
}

function TaskListViewModel() {
  // Data
  var self = this;
  self.tasks = ko.observableArray([]);
  self.newTaskText = ko.observable();
}



function loadData() {

}

window.addEventListener('load', loadData)