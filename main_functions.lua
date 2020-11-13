function search_table(itemname)
    for index, value in next, Donkey_loot_table do
        if value["loot_id"] == itemname then
            return value["prio"]
        end
    end
end