function cum_search_table(itemname)
    for index, value in next, Loading_bis_table do
        if value["loot_id"] == itemname then
            return value["prio"]
        end
    end
end
