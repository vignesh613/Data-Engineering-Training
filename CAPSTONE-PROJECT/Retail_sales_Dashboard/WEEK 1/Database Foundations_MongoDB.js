// MONGODB SCRIPT FOR WEEK 1: CAMPAIGN DATA AND INDEXING
// Objective: Store promotional campaign feedback and add indexes for fast searching.

// 1. DATABASE AND COLLECTION SETUP
// --------------------------------------------------------------------------------
// Use the desired database. If it doesn't exist, MongoDB creates it.
use RetailSalesAnalytics

// 2. STORE CAMPAIGN FEEDBACK (Unstructured Data)
// --------------------------------------------------------------------------------
// Store promotional campaign feedback in MongoDB[cite: 10, 13].
db.campaignFeedback.insertMany([
    {
        campaign_id: "SUMMER_2024",
        store_id: 101,
        date: new Date("2024-07-15T10:00:00Z"),
        feedback_type: "customer_comment",
        notes: "Long lines due to the 50% off electronics deal. Customers were happy with the 'Laptop Pro' sale.",
        sentiment: "positive",
        product_focus: ["Laptop Pro"],
        region: "North"
    },
    {
        campaign_id: "FALL_PREP",
        store_id: 102,
        date: new Date("2024-09-01T15:30:00Z"),
        feedback_type: "employee_report",
        notes: "Region South sales team noted low traffic after the first week.",
        sentiment: "negative",
        region: "South"
    },
    {
        campaign_id: "SUMMER_2024",
        store_id: 101,
        date: new Date("2024-07-20T11:45:00Z"),
        feedback_type: "website_survey",
        notes: "Great deals, very satisfied with the checkout process.",
        sentiment: "positive",
        region: "North"
    }
])

// 3. INDEXING
// --------------------------------------------------------------------------------
// Add indexes to search by product and region[cite: 11, 13].

// Index 1: Index on 'product_focus' (to search by product)
db.campaignFeedback.createIndex({ product_focus: 1 })

// Index 2: Index on 'region' (to search by region)
db.campaignFeedback.createIndex({ region: 1 })

// Optional: View the indexes created
// db.campaignFeedback.getIndexes()