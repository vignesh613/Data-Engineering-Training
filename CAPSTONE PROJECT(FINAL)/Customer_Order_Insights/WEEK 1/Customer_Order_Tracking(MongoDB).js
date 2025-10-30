
// ===============================
// Week 1 - MongoDB Script
// ===============================

use customer_order_tracker

// Insert Feedback Documents
db.feedback.insertMany([
  { customer_id: 1, feedback: "Laptop delivered late but works fine.", rating: 3, date: new Date("2025-09-05") },
  { customer_id: 2, feedback: "Mobile phone was packed well.", rating: 4, date: new Date("2025-09-06") },
  { customer_id: 3, feedback: "Headphones were defective.", rating: 2, date: new Date("2025-09-07") },
  { customer_id: 4, feedback: "Smart watch excellent.", rating: 5, date: new Date("2025-09-08") },
  { customer_id: 5, feedback: "Tablet too slow.", rating: 2, date: new Date("2025-09-09") },
  { customer_id: 6, feedback: "Shoes stylish.", rating: 4, date: new Date("2025-09-10") },
  { customer_id: 7, feedback: "Refrigerator cooling well.", rating: 5, date: new Date("2025-09-11") },
  { customer_id: 8, feedback: "Microwave stopped working.", rating: 1, date: new Date("2025-09-12") },
  { customer_id: 9, feedback: "AC installation delayed.", rating: 3, date: new Date("2025-09-13") },
  { customer_id: 10, feedback: "Washing machine superb.", rating: 5, date: new Date("2025-09-14") },
  { customer_id: 11, feedback: "Books were damaged.", rating: 1, date: new Date("2025-09-15") },
  { customer_id: 12, feedback: "TV screen excellent.", rating: 5, date: new Date("2025-09-16") },
  { customer_id: 13, feedback: "Shoes did not fit.", rating: 2, date: new Date("2025-09-17") },
  { customer_id: 14, feedback: "Bag durable.", rating: 4, date: new Date("2025-09-18") },
  { customer_id: 15, feedback: "Camera too costly.", rating: 3, date: new Date("2025-09-19") },
  { customer_id: 16, feedback: "Printer good quality.", rating: 4, date: new Date("2025-09-20") },
  { customer_id: 17, feedback: "Keyboard keys stuck.", rating: 2, date: new Date("2025-09-21") },
  { customer_id: 18, feedback: "Monitor crystal clear.", rating: 5, date: new Date("2025-09-22") },
  { customer_id: 19, feedback: "Power bank works well.", rating: 4, date: new Date("2025-09-23") },
  { customer_id: 20, feedback: "Router disconnects often.", rating: 2, date: new Date("2025-09-24") }
]);

// Indexes
db.feedback.createIndex({ customer_id: 1 });
db.feedback.createIndex({ rating: 1 });
db.feedback.createIndex({ date: -1 });
db.feedback.createIndex({ customer_id: 1, rating: -1 });
db.feedback.createIndex({ feedback: "text" });
