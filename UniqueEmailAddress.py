class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int

        address = list()
        for i in emails:
            i_list = list(i)
            if '+' in i_list:
                for j in range(0, len(i_list)):
                    if i_list[j] == '+':
                        endpos = 0
                        for k in range(j, len(i_list)):
                            if i_list[k] == '@':
                                endpos = k
                                break
                        local_addr = i_list[0:j]
                        break
                while '.' in local_addr:
                    local_addr.remove('.')
                new_addr = local_addr + i_list[endpos:len(i_list)]
                if "".join(new_addr) not in address:
                    address.append("".join(new_addr))
                    continue
            else:
                for j in range(0, len(i_list)):
                    if i_list[j] == '@':
                        break
                    elif i_list[j] == '.':
                        i_list.pop(j)
                "".join(i_list)
                if "".join(i_list) not in address:
                    address.append("".join(i_list))
        return len(address)
        """
        address = list()
        count = 0
        for i in emails:
            addr = i.split('@')
            local = addr[0][0:addr[0].find('+')]
            local_addr = local.replace(".","")
            addr = local_addr + '@' + addr[1]
            if addr not in address:
                address.append(addr)
                count += 1
        return count
  


