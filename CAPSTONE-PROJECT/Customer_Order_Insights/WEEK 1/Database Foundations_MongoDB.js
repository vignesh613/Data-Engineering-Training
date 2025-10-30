// 1. Switch to (or create) the appropriate database
use customer_order_insights_db; 

// 2. Insert Sample Customer Feedback (Unstructured Data)
// This fulfills the task: "Store customer feedback (unstructured) in MongoDB" [cite: 9]
db.customer_feedback.insertMany([
    {
        customer_id: 1,
        order_id: 101,
        rating: 2,
        feedback_type: "Complaint",
        feedback_text: "The package was late and arrived damaged. Poor delivery service.",
        received_date: new Date("2025-10-15")
    },
    {
        customer_id: 1,
        order_id: 105,
        rating: 5,
        feedback_type: "Praise",
        feedback_text: "Fastest delivery ever! I'm very happy with this order.",
        received_date: new Date("2025-10-10")
    },
    {
        customer_id: 2,
        order_id: 210,
        rating: 4,
        feedback_type: "Suggestion",
        feedback_text: "The delivery tracking map could be more accurate.",
        received_date: new Date("2025-10-14")
    }
]);

// 3. Create Index on customer_id
// This fulfills the task: "Index MongoDB collection to search by customer ID" [cite: 10]
db.customer_feedback.createIndex({ customer_id: 1 });

// 4. Verification (Optional: Check the index was created)
// db.customer_feedback.getIndexes();

// 5. Example Search (Optional: Test the indexed search)
// db.customer_feedback.find({ customer_id: 1 }).pretty();