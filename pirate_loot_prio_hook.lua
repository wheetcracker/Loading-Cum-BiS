BINDING_HEADER_DKP = "Loading Pirates BiS";

GameTooltip:HookScript("OnTooltipSetItem", function(tooltip, ...)
  local itemname, itemlink = tooltip:GetItem()
  
  if itemlink then

	priority = pirate_search_table(itemlink:match("item:(%d+):"))
  
  end
 
  if priority then
    prio = string.format(" %s", priority)
    splitprio = split(prio, ",")

    tooltip:AddLine(" ")
    tooltip:AddLine("Team Pirate BiS:", 1, 0, 0.5)

    for index, prioLevel in pairs(splitprio) do 
      line = " " .. prioLevel
      tooltip:AddLine(line, 1, 0, 0.5, true)
    end
  
end
end)

ItemRefTooltip:HookScript("OnTooltipSetItem", function(tooltip, ...)local itemname, itemlink = tooltip:GetItem()
  
  if itemlink then

	priority = pirate_search_table(itemlink:match("item:(%d+):"))

  end
  
  if priority then
    prio = string.format(" %s", priority)
    splitprio = split(prio, ",")

    tooltip:AddLine(" ")
    tooltip:AddLine("Team Pirate BiS:", 1, 0, 0.5)

    for index, prioLevel in pairs(splitprio) do 
      line = " " .. prioLevel
      tooltip:AddLine(line, 1, 0, 0.5, true)
    end
	
  end
  end)

function split(s, sep)
  local fields = {}
  
  local sep = sep or " "
  local pattern = string.format("([^%s]+)", sep)
  string.gsub(s, pattern, function(c) fields[#fields + 1] = c end)
  
  return fields
end
