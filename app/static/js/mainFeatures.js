var initialData = [{
  client_id: 1,
  client_name: "Topher",
  description: "Please add a front-end",
  id: 1,
  priority: 1,
  productArea_id: 1,
  productArea_name: "Front-end",
  submitter_id: 1,
  submitter_name: "Chris Lichter",
  targetDate: "01-01-2018",
  title: "Front-end"
}]

function Feature(data) {
  this.id = ko.observable(data.id);
  this.title = ko.observable(data.title);
  this.description = ko.observable(data.description);
  this.client_id = ko.observable(data.client_id);
  this.client_name = ko.observable(data.client_name);
  this.priority = ko.observable(data.priority);
  this.targetDate = ko.observable(data.targetDate);
  this.productArea_id = ko.observable(data.productArea_id);
  this.productArea_name = ko.observable(data.productArea_name);
  this.submitter_id = ko.observable(data.submitter_id);
  this.submitter_name = ko.observable(data.submitter_name);
}

var FeatureModel = function() {
  var self = this;
  self.featuresArray = ko.observableArray([]);

  $.getJSON("/features", function(data) {
    var mappedFeatures = $.map(data.features, function(item) {
      return new Feature(item)
    });
    self.featuresArray(mappedFeatures);
  });
};

ko.applyBindings(new FeatureModel());