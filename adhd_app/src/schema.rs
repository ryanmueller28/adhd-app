// @generated automatically by Diesel CLI.

diesel::table! {
    recipes (id_recipe) {
        id_recipe -> Uuid,
        id_user -> Nullable<Uuid>,
        title -> Varchar,
        body -> Varchar,
        published -> Bool,
    }
}

diesel::table! {
    users (id_user) {
        id_user -> Uuid,
        username -> Varchar,
        password_hash -> Varchar,
        email -> Varchar,
        first_name -> Nullable<Varchar>,
        last_name -> Nullable<Varchar>,
        dob -> Timestamp,
    }
}

diesel::joinable!(recipes -> users (id_user));

diesel::allow_tables_to_appear_in_same_query!(
    recipes,
    users,
);
