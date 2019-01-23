
chrome.browserAction.onClicked.addListener(function(activeTab)
{
    var newURL = "popup.html";
    chrome.tabs.create({ url: newURL });
});

// Code for changing tabs
let selectTab = (direction) => {
    chrome.tabs.query({
        currentWindow: true
    }, (tabs) => {
        if (tabs.length <= 1) {
            return
        }
        chrome.tabs.query({
            currentWindow: true,
            active: true
        }, (currentTabInArray) => {
            let currentTab = currentTabInArray[0]
            let toSelect
            switch (direction) {
                case 'next':
                    toSelect = tabs[(currentTab.index + 1 + tabs.length) % tabs.length]
                    break
                case 'previous':
                    toSelect = tabs[(currentTab.index - 1 + tabs.length) % tabs.length]
                    break
                case 'first':
                    toSelect = tabs[0]
                    break
                case 'last':
                    toSelect = tabs[tabs.length - 1]
                    break
                default:
                    let index = parseInt(direction) || 0
                    if (index >= 1 && index <= tabs.length) {
                        toSelect = tabs[index - 1]
                    } else {
                        return
                    }
            }
            chrome.tabs.update(toSelect.id, {
                active: true
            })
        })
    })
}


// Code for click events
let handleAction = (action, request = {}) => {

    if (action === 'nexttab') {
        selectTab('next')
    } else if (action === 'prevtab') {
        selectTab('previous')
    } else if (action === 'scrollup') {
        chrome.tabs.executeScript(null, {
            'code': 'window.scrollBy(0,-50)'
        })
    } else if (action === 'scrolldown') {
        chrome.tabs.executeScript(null, {
            'code': 'window.scrollBy(0,50)'
        })
    } else if (action === 'newprivatewindow') {
        chrome.windows.create({incognito: true})
    } else if (action === 'zoomin') {
        chrome.tabs.query({currentWindow: true, active: true}, (tab) => {
          chrome.tabs.getZoom(tab[0].id, (zoomFactor) => {
            console.log(zoomFactor)
            chrome.tabs.setZoom(tab[0].id, zoomFactor + 0.1)
          })
        })
    } else if (action === 'zoomout') {
        chrome.tabs.query({currentWindow: true, active: true}, (tab) => {
          chrome.tabs.getZoom(tab[0].id, (zoomFactor) => {
            chrome.tabs.setZoom(tab[0].id, zoomFactor - 0.1)
          })
        })
      } else {
        return false
    }
    return true
}
